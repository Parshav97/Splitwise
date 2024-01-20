from model.UsersModel import UsersModel
from model.ExpenseTransactionsModel import ExpenseTransactionsModel
from controller.UserController import UserController
from flask import Blueprint, request, jsonify

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route("/register", methods=['POST'])
def register():
    try:
        dataObj = {
            "name":request.body.name,
            "email":request.body.email,
            "mobile":request.body.mobile
        }
        controller = UserController()
        userObj = controller.create_new_user(dataObj)
        return jsonify(userObj)
    except:
        print("Unable to Create User")


@user_blueprint.route("/get-all")
def list():
    try:
        controller = UserController()
        list_of_users = controller.fetch_all_users()
        return jsonify(list_of_users)
    except:
        print("Unable to List User")

@user_blueprint.route("/all-expenses-to-pay/<user_id>")
def expenses(user_id):
    try:
        controller = UserController()
        list_of_expenses = controller.fetch_user_expenses_to_pay(user_id)
        return jsonify(list_of_expenses)
    except:
        print("Unable to Fetch Expenses")


@user_blueprint.route("/all-expenses-to-receive/<user_id>")
def payments(user_id):
    try:
        controller = UserController()
        list_of_expenses = controller.fetch_user_balance_to_receive(user_id)
        return jsonify(list_of_expenses)
    except:
        print("Unable to Fetch payments")


@user_blueprint.route("/settle-up/<trans_id>", methods=["POST"])
def settle_up(trans_id):
    try:
        controller = UserController()
        controller.settle_up(trans_id)
        return jsonify({"status":"Transaction Settled Successully"})
    except:
        print("Unable to Settle Tranasaction")