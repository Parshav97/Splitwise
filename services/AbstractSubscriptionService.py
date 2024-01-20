from abc import ABC, abstractmethod

class AbstractSubscriptionService(ABC):

    @abstractmethod
    def on_expense_creation(self, args):
        pass
    