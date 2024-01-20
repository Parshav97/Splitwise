from strategy.PercentageSplitStrategy import PercentageSplitStrategy
from strategy.ExactSplitStrategy import ExactSplitStrategy
from strategy.EqualSplitStrategy import EqualSplitStrategy
from model.ExpenseTypeModel import ExpenseTypeModel

class ExpenseSplitFactory:

    def __init__(self):
        pass

    def selectStrategy(self, data):
        strategy = None
        if data.type == ExpenseTypeModel.PERCENTAGE:
            strategy = PercentageSplitStrategy()
        elif data.type == ExpenseTypeModel.EXACT:
            strategy = ExactSplitStrategy()
        elif data.type == ExpenseTypeModel.EQUAL:
            strategy = EqualSplitStrategy()

        return strategy