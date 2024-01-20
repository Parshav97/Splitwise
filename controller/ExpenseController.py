from services.ExpenseCreationService import ExpenseCreationService
from dotenv import load_dotenv
import os
load_dotenv()

MAX_AMOUNT = os.getenv("MAX_AMOUNT")

class ExpenseController():
    exp_service = None
    def __init__(self):
        self.exp_service = ExpenseCreationService

    def createExpense(self,data):
        try:
            if(data.amount <= 0 or data.amount>MAX_AMOUNT):
                raise Exception("Invalid amount mentioned for the Expense")
            exp_service = self.exp_service()
            responseObj = exp_service.create_expense(data)
            return responseObj
        except:
            print("Please Enter a value less than {}".format(MAX_AMOUNT))
            
