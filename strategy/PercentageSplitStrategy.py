from strategy.ExpenseSplitStrategy import Expense_Splitting_Strategy
class PercentageSplitStrategy(Expense_Splitting_Strategy):

    def split(self, args):
        try:
            arr = args[0]
            if( sum(arr) != 100):
                raise Exception("Sum percentages is not 100")
            amount = args[1]
            brr = list(map(lambda x : x /100, arr))
            ans = list(map(lambda x : x*amount, brr))
            return ans
        except:
            print("Error in Implementing PercentageSplitStrategy")
            
        