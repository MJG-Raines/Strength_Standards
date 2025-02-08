from decimal import Decimal
from ..core.enums import BenchWeightClass, AgeCategory

def get_age_category(age: int) -> AgeCategory:
    """
    Takes age, returns the correct age category.
    """
    if 20 <= age <= 23:
        return AgeCategory.JUNIOR_20_23
    elif 24 <= age <= 34:
        return AgeCategory.OPEN_24_34
    elif 35 <= age <= 39:
        return AgeCategory.SUBMASTER_35_39
    elif 40 <= age <= 44:
        return AgeCategory.MASTER_40_44
    elif 45 <= age <= 49:
        return AgeCategory.MASTER_45_49
    elif 50 <= age <= 54:
        return AgeCategory.MASTER_50_54
    elif 55 <= age <= 59:
        return AgeCategory.MASTER_55_59
    elif 60 <= age <= 64:
        return AgeCategory.MASTER_60_64
    elif 65 <= age <= 69:
        return AgeCategory.MASTER_65_69
    elif 70 <= age <= 74:
        return AgeCategory.MASTER_70_74
    elif age >= 75:
        return AgeCategory.MASTER_75_79

def get_weight_class(weight: Decimal, sex: str) -> BenchWeightClass:
    """
    Takes weight in pounds and sex (M/F), returns correct weight class.
    """
    if sex == 'M':
        if weight <= 114:
            return BenchWeightClass.M_114
        elif weight <= 123:
            return BenchWeightClass.M_123
        elif weight <= 132:
            return BenchWeightClass.M_132
        elif weight <= 148:
            return BenchWeightClass.M_148
        elif weight <= 165:
            return BenchWeightClass.M_165
        elif weight <= 181:
            return BenchWeightClass.M_181
        elif weight <= 198:
            return BenchWeightClass.M_198
        elif weight <= 220:
            return BenchWeightClass.M_220
        elif weight <= 242:
            return BenchWeightClass.M_242
        elif weight <= 275:
            return BenchWeightClass.M_275
        elif weight <= 308:
            return BenchWeightClass.M_PLUS
        else:
            return BenchWeightClass.M_Max
    
    elif sex == 'F':
        if weight <= 97:
            return BenchWeightClass.W_97
        elif weight <= 105:
            return BenchWeightClass.W_105
        elif weight <= 114:
            return BenchWeightClass.W_114
        elif weight <= 123:
            return BenchWeightClass.W_123
        elif weight <= 132:
            return BenchWeightClass.W_132
        elif weight <= 148:
            return BenchWeightClass.W_148
        elif weight <= 165:
            return BenchWeightClass.W_165
        elif weight <= 181:
            return BenchWeightClass.W_181
        elif weight <= 198:
            return BenchWeightClass.W_198
        else:
            return BenchWeightClass.W_PLUS