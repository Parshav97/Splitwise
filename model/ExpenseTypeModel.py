from enum import Enum

class ExpenseTypeModel(Enum):
    EXACT = "EXACT"
    EQUAL = "EQUAL"
    PERCENTAGE = "PERCENTAGE"