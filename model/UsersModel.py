from model.sqlalchemy import db
import uuid

class UsersModel(db.Model):
    id = db.Column(db.String(20), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(20))
    mobile_no = db.Column(db.String(10))
    email_id = db.Column(db.String(20))