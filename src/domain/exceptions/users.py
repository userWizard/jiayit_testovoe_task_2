from dataclasses import dataclass

from src.domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class NameValueException(ApplicationException):
    text: str
    
    @property
    def message(self):
        return f'The field {self.text} contains incorrect characters.'

@dataclass(eq=False)
class EmailValueException(ApplicationException):
    text: str
    
    @property
    def message(self):
        return f'The field {self.text} contains an invalid email address.'

@dataclass(eq=False)
class IdValueException(ApplicationException):
    @property
    def message(self):
        return 'The field is not a valid type or zero.'