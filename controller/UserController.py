from services.UserService import UserService

class UserController:
    user_service = None

    def __init__(self):
        self.user_service = UserService

    def create_new_user(self, dataObj):
        try:
            userObj = self.user_service.register(dataObj)
            return userObj
        except:
            print("User Service Unable to Create User")

    def fetch_all_users(self):
        try:
            users_list = self.user_service.get_all()
            return users_list
        except:
            print("User Service Unable to Fetch User")

    def fetch_user_expenses_to_pay(self, user_id):
        try:
            transactions = self.user_service.expenses_to_pay(user_id)
            return transactions
        except:
            print("User Service Unable to Fetch Expenses")

    def fetch_user_balance_to_receive(self, user_id):
        try:
            transactions = self.user_service.expenses_to_receive(user_id)
            return transactions
        except:
            print("User Service Unable to Fetch Payments")

    def settle_up(self, transaction_id):
        try:
            self.user_service.settle_up(transaction_id)
        except:
            print("User Service Unable to Settle Up")
