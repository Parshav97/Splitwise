from abc import ABC, abstractmethod
class Expense_Splitting_Strategy(ABC):
    @abstractmethod
    def split(self, args):
        pass
