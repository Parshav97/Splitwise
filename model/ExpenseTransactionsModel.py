from model.sqlalchemy import db
import uuid
from sqlalchemy import ForeignKey
from model.ExpensesModel import ExpensesModel
from model.UsersModel import UsersModel
from model.TransactionStatusModel import TransactionStatus

class ExpenseTransactionsModel(db.Model):
    id = db.Column(db.String(20), primary_key=True, default=uuid.uuid4)
    expense_id = db.Column(db.String(20), ForeignKey(ExpensesModel.id) )
    receiver_id = db.Column(db.String(20), ForeignKey(UsersModel.id))
    payer_id = db.Column(db.String(20), ForeignKey(UsersModel.id))
    amount = db.Column(db.Integer)
    status_id = db.Column(db.Enum(TransactionStatus))

