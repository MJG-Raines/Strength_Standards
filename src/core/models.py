from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator
from decimal import Decimal

from .enums import LiftType, BenchWeightClass, AgeCategory

class Athlete(BaseModel):
    """
    Core athlete model. All weights in pounds.
    Tracking weight history for bodyweight exercises.
    """
    id: str
    name: str
    birthdate: date
    sex: str = Field(..., pattern="^[MF]$")
    
    # Weight tracking in pounds
    current_weight: Decimal = Field(..., decimal_places=2)
    weight_history: list[dict[date, Decimal]] = []
    
    # Optional social
    instagram: Optional[str] = None
    
    class Config:
        from_attributes = True

class LiftResult(BaseModel):
    """
    Handles both flat weight (bench) and bodyweight + weight (dips/pullups).
    All weights stored in pounds.
    """
    id: str
    athlete_id: str
    lift_type: LiftType
    
    # Core lift data
    weight_lifted: Decimal = Field(..., gt=0, decimal_places=2)  # Total weight or added weight
    bodyweight: Decimal = Field(..., gt=0, decimal_places=2)     # Current bodyweight
    date: date
    
    # For weighted bodyweight exercises
    is_bodyweight_plus: bool = False  # True for pullups/dips
    reps: int = Field(1, ge=1)       # Single rep for now, might expand later
    
    # Validation
    video_url: Optional[str] = None
    form_rating: Optional[int] = Field(None, ge=1, le=5)  # For strict curl form validation
    verified: bool = False
    verified_by: Optional[str] = None
    
    @validator('weight_lifted')
    def validate_weight(cls, v, values):
        """
        Validates weights make sense for the lift type.
        For bodyweight exercises, weight_lifted is the added weight only.
        """
        if 'lift_type' in values:
            if values['lift_type'] in [LiftType.PULLUP, LiftType.DIP]:
                if not values.get('is_bodyweight_plus'):
                    raise ValueError("Bodyweight exercises must be marked as bodyweight_plus")
                if v > 500:  # No one's adding 500lbs to a pullup/dip
                    raise ValueError("Added weight for bodyweight exercise seems too high")
            elif values['lift_type'] == LiftType.BENCH:
                if v > 1500:  # World record territory
                    raise ValueError("Bench press weight seems too high")
            elif values['lift_type'] == LiftType.CURL:
                if v > 500:  # Even this is superhuman
                    raise ValueError("Strict curl weight seems too high")
        return v
    
    @validator('bodyweight')
    def validate_bodyweight(cls, v):
        """Basic sanity check for bodyweight"""
        if v < 50 or v > 600:  # Range for human bodyweights
            raise ValueError("Bodyweight seems out of normal human range")
        return v
    
    class Config:
        from_attributes = True

class PersonalBest(BaseModel):
    """
    Tracks personal records for each lift type.
    Separate from LiftResult to easily query PRs.
    """
    athlete_id: str
    lift_type: LiftType
    weight_class: str  # Stored as string since different lifts use different classes
    age_category: AgeCategory
    best_result: Decimal
    achieved_date: date
    lift_result_id: str  # Reference to the actual lift
    
    class Config:
        from_attributes = True