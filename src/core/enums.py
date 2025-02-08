from enum import Enum

class LiftType(Enum):
    # Core lift
    BENCH = "bench_press"
    
    # Planned expansion lifts to track - each with own weight class logic
    CURL = "strict_curl"      
    PULLUP = "weighted_pullup"  
    DIP = "weighted_dip"      
    
    def __str__(self):
        return self.value

class BenchWeightClass(Enum):
    # Men's weight classes (in lbs)
    M_114 = "M_114"    # -114 
    M_123 = "M_123"    # -123 
    M_132 = "M_132"    # -132 
    M_148 = "M_148"    # -148 
    M_165 = "M_165"    # -165 
    M_181 = "M_181"    # -181 
    M_198 = "M_198"    # -198 
    M_220 = "M_220"    # -220 
    M_242 = "M_242"    # -242 
    M_275 = "M_275"    # -275 
    M_PLUS = "M_308"  #  -308
    M_Max =  "M_+308" # +308
    
    # Women's weight classes (in lbs)
    W_97 = "W_97"      # -97 
    W_105 = "W_105"    # -105 
    W_114 = "W_114"    # -114 
    W_123 = "W_123"    # -123 
    W_132 = "W_132"    # -132 
    W_148 = "W_148"    # -148 
    W_165 = "W_165"    # -165 
    W_181 = "W_181"    # -181 
    W_198 = "W_198"    # -198 
    W_PLUS = "W_198+"  # 198+ 

class CurlWeightClass(Enum):
    """Placeholder - will be updated with official strict curl classes"""
    pass

class PullupWeightClass(Enum):
    """
    Placeholder - might be based on bodyweight ratios
    or total weight (bodyweight + added weight)
    """
    pass

class DipWeightClass(Enum):
    """
    Placeholder - might be based on bodyweight ratios
    or total weight (bodyweight + added weight)
    """
    pass

class AgeCategory(Enum):
    # Following powerlifting age brackets to make it easy
    JUNIOR_20_23 = "junior_20_23"  # 20-23
    SENIOR_24_34 = "senior_24_34"      # 24-34
    SUBMASTER_35_39 = "sm_35_39"   # 35-39
    MASTER_40_44 = "m1_40_44"      # 40-44
    MASTER_45_49 = "m1_45_49"      # 45-49
    MASTER_50_54 = "m2_50_54"      # 50-54
    MASTER_55_59 = "m2_55_59"      # 55-59
    MASTER_60_64 = "m3_60_64"      # 60-64
    MASTER_65_69 = "m3_65_69"      # 65-69
    MASTER_70_74 = "m4_70_74"      # 70-74
    MASTER_75_79 = "m4_75_79"      # 75-79

class Equipment(Enum):
    RAW = "raw"              # The only way
    

def get_weight_class_enum(lift_type: LiftType) -> type[Enum]:
    """Returns appropriate weight class enum based on lift type"""
    weight_class_map = {
        LiftType.BENCH: BenchWeightClass,
        LiftType.CURL: CurlWeightClass,
        LiftType.PULLUP: PullupWeightClass,
        LiftType.DIP: DipWeightClass
    }
    return weight_class_map.get(lift_type)