from strategy.ExpenseSplitStrategy import Expense_Splitting_Strategy
class EqualSplitStrategy(Expense_Splitting_Strategy):

    def split(self, args):
        try:
            arr = args[0]
            amount = args[1]
            b = [round(1/len(arr),2)]*len(arr)
            bsum = sum(b)
            if bsum < 1.00:
                count = 0
                while(bsum < 1.00):
                    b[count] += 0.01
                    count += 1
                    bsum += 0.01
            elif bsum > 1.00:
                count = 0
                while(bsum > 1.00):
                    b[count] -= 0.01
                    count += 1
                    bsum -= 0.01
            
            ans = list(map(lambda x : x*amount, b))
            return ans
        except:
            print("Error in Implementing EqualSplitStrategy")

        
            
        