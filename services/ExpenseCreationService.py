from model.ExpensesModel import ExpensesModel
# from model.UsersExpensesModel import UsersExpensesModel
from model.ExpenseTransactionsModel import ExpenseTransactionsModel

from model.TransactionStatusModel import TransactionStatus

from factory.ExpenseSplitFactory import ExpenseSplitFactory

from flask import jsonify
from model.sqlalchemy import db
from datetime import datetime

class ExpenseCreationService:
    expenses_model = None
    exp_tran_model = None
    email_service = None

    subscription_services_list = []
    def __init__(self):
        self.expenses_model = ExpensesModel
        self.exp_tran_model = ExpenseTransactionsModel

    def send_mail(self, expense, expense_trans_lis):
        for subscriber in ExpenseCreationService.subscription_services_list:
            subscriber.on_expense_creation(expense, expense_trans_lis)


    def create_expense(self,data):
        try:
            
            strategy = ExpenseSplitFactory.selectStrategy(data)
            amounts_arr = strategy.split(data.users_ratio, data.amount)

            expense = self.expenses_model(
                name = data.name,
                amount = data.amount,
                date_time = datetime.now(),
                type = data.type,
                paid_by = data.paid_by
            )

            lis = []
            lis_exp_trans_id = []
            for i in range(0,len(data.users)):
                each_user = data.users[i]
            
                if each_user != expense.paid_by:
                    exp_trans = self.exp_tran_model(
                        expense_id = expense.id,
                        receiver_id = expense.paid_by,
                        payer_id = each_user,
                        amount = amounts_arr[i],
                        status_id = TransactionStatus.PENDING
                    )
                    lis.append(exp_trans)
                    lis_exp_trans_id.append(exp_trans.id)
                    
            
            db.session.add(expense)
            db.session.add_all(lis)
            db.session.commit()

            self.send_mail(expense, lis)

            return {"exp_id":expense.id, "lis_exp_trans_id": lis_exp_trans_id}

        except:
            print("Error Encountered while creating an expence")



