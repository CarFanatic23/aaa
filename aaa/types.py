# Types
from .error import RuntimeError

class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start = None, pos_end = None):
        '''Set position.'''
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context = None):
        '''Set context.'''
        self.context = context
        return self

    def add(self, other_num):
        '''Add to another number.'''
        if isinstance(other_num, Number):
            return Number(
                self.value + other_num.value
            ).set_context(self.context)

    def sub(self, other_num):
        '''Subract by another number.'''
        if isinstance(other_num, Number):
            return Number(
                self.value - other_num.value
            ).set_context(self.context)

    def mul(self, other_num):
        '''Multiply by another number.'''
        if isinstance(other_num, Number):
            return Number(
                self.value * other_num.value
            ).set_context(self.context)

    def pow(self, other_num):
        '''Exponent by another number.'''
        if isinstance(other_num, Number):
            return Number(
                self.value ** other_num.value
            ).set_context(self.context)

    def div(self, other_num):
        '''Divide by another number.'''
        if isinstance(other_num, Number):
            if other_num.value == 0:
                return None, RuntimeError(
                    other_num.pos_start,
                    other_num.pos_end,
                    'Division by zero.',
                    self.context
                )
            return Number(
                self.value / other_num.value
            ).set_context(self.context), None

    def __repr__(self):
        return str(self.value)
