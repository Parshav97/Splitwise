from flask import Blueprint, jsonify, request
from controller import ExpenseController

expense_blueprint = Blueprint('expense_blueprint', __name__)

@expense_blueprint.route("/create-expense", methods=["POST"])
def create_expense():
    dataObj = {
        "name":request.body.name,
        "amount": request.body.amount,
        "type":request.body.type,
        "paid_by":request.body.paid_by,
        "users":request.body.users,
        "users_ratio":request.body.users_ratio
    }
    controller = ExpenseController()
    expense_exp_trans = controller.createExpense(dataObj)
    return jsonify(expense_exp_trans)
    


