from strategy.ExpenseSplitStrategy import Expense_Splitting_Strategy
class ExactSplitStrategy(Expense_Splitting_Strategy):

    def split(self, args):
        try:
            arr = args[0]
            amount = args[1]
            if(sum(arr) != amount):
                raise Exception("Sum of each user amount owed is not equal to sum paid")
            return arr
        
        except:
            print("Error in Implementing ExactSplitStrategy")
        