from model.sqlalchemy import db
import uuid
from datetime import datetime
from model.ExpenseTypeModel import ExpenseTypeModel
from model.UsersModel import UsersModel
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.sql import func


class ExpensesModel(db.Model):
    id = db.Column(db.String(20), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(10))
    amount = db.Column(db.Integer)
    date_time = db.Column(DateTime())
    type = db.Column(db.Enum(ExpenseTypeModel))
    paid_by = db.Column(db.String(20), ForeignKey(UsersModel.id))