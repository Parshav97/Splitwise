from model.UsersModel import UsersModel
from model.ExpenseTransactionsModel import ExpenseTransactionsModel
from model.TransactionStatusModel import TransactionStatus
from flask import jsonify 
from model.sqlalchemy import db

class UserService:
    user_model = None
    exp_trans_model = None
    def __init__(self):
        self.user_model = UsersModel
        self.exp_trans_model = ExpenseTransactionsModel

    def register(self, data):
        try:
            user = self.user_model(
                name = data.name,
                mobile_no = data.mobile,
                email_id = data.email
            )
            db.session.add(user)
            db.session.commit()

            return {"user_id":user.id}
        except:
            print("Error registering a user")

    def get_all(self):
        try:
            all_users = self.user_model.query.all()
            return {"users":all_users}
        except:
            print("Error Occured in etching the data")
    
    def expenses_to_pay(self, user_id):
        try:
            pending_trans = self.exp_trans_model.query.filter_by(payer_id=user_id, status_id=TransactionStatus.PENDING).all()
            return {"transactions":pending_trans}
        except:
            print("Error Occured in Fetching User's Pending Expenses")
        
    def expenses_to_receive(self, user_id):
        try:
            pending_payments = self.exp_trans_model.query.filter_by(receiver_id=user_id, status_id=TransactionStatus.PENDING).all()
            return {"transactions":pending_payments}
        except:
            print("Error Occured in Fetching User's Pending Payments")
        
    def settle_up(self, trans_id):
        try:
            transaction = self.exp_trans_model.query.filter(id=trans_id)
            transaction.status_id = TransactionStatus.SUCCESSFUL
            db.session.commit()

        except:
            print("Error in settling up the database")
        