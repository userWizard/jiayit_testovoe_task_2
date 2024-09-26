import re
from dataclasses import dataclass

from src.domain.exceptions.users import (
    NameValueException,
    EmailValueException,
    IdValueException,
)
from src.domain.values.base import BaseValueObject
from src.common.temps import (
    NAME,
    EMAIL,
    VALUE,
)


@dataclass(frozen=True)
class Name(BaseValueObject):
    value: str
    
    def valiadte(self):
        if not re.match(NAME, self.value):
            raise NameValueException(self.value)

    def as_generic_type(self):
        return str(self.value)

@dataclass(frozen=True)
class Email(BaseValueObject):
    value: str
    
    def validate(self):
        if not re.match(EMAIL, self.value):
            raise EmailValueException(self.value)
    
    def as_generic_type(self):
        return str(self.value)

@dataclass(frozen=True)
class Id(BaseValueObject):
    value: int
    
    def validate(self):
        if not isinstance(self.value, int) or self.value <= VALUE:
            raise IdValueException('Invalid id type.')

    def as_generic_type(self):
        return int(self.value)