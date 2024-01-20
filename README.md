SCHEMA DESIGN
USERS
Id | name | mobile_no | emai_id
EXPENSES
Id | name | amount | datetime | type
EXPENSE_TRANSACTIONS
Id | expense_id | receiver_id | payer_id | amount | status_id

CLASS DIAGRAM
Strategy
abstract class ExpenseSplitStrategy
@abstractmethod
def split()

class EqualSplitStrategy(ExpenseSplitStrategy)
@override
def split()

class ExactSplitStrategy(ExpenseSplitStrategy)
@override
def split()

class PercentageSplitStrategy(ExpenseSplitStrategy)
@override
def split()

Service
abstract class AbstractSubscriptionService
@abstractmethod
def on_expense_creation()

class EmailService(AbstractSubscriptionService)
def on_expense_creation():
		#code

class ExpenseCreationService:
	def create_expense():
		#code
	def send_email():
		#code

class UserService:
	def register()
	def get_all()
	def expenses_to_pay()
	def expenses_to_receive()
	def settle_up()

Models
class UsersModel:
	id
	name
	mobile_no
	email_id
class ExpensesModel:
	id
name
amount
date_time
type
paid_by
class ExpenseTransactionModel:
	id
	expense_id
	receiver_id
	payer_id
	amount
	status_id
class TransactionStatus(ENUM):
	PENDING
	SUCCESSFUL
class ExpenseTypeModel(ENUM):
	EXACT
	EQUAL
	PERCENTAGE












File Structure
![image](https://github.com/Parshav97/Splitwise/assets/47355647/ad384074-3d57-422c-8ba8-49eada4cf2c4)

 

API Contracts

1)	POST: http://localhost:5000/create-expense
BODY:
{
	“name”:”dinner”
	“amount”:5000
	“type”: “EQUAL”
	“paid_by”: “u1”
	“users” : [ “u1”, “u2”, “u3”, “u4”]
	“users_ratio” : [1, 1, 1, 1]
}

2)	POST: http://localhost:5000/register
BODY:
{
	“name”:”anup”
	“email”:”ab@gmail.com”
	“mobile”: “9999999999”
}

3)	GET: http://localhost:5000/get-all
4)	GET: http://localhost:5000/all-expenses-to-pay/<user_id>
5)	GET: http://localhost:5000/all-expenses-to-receive/<user_id>
6)	POST: http://localhost:5000/settle-up/<trans_id>




Architecture Diagram
 
![image](https://github.com/Parshav97/Splitwise/assets/47355647/fbb09cd5-77be-47b5-b51e-7846e713c5dd)
