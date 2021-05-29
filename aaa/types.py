# Types

class Number:
    def __init__(self, value):
        self.value = value

    def set_pos(self, pos_start = None, pos_end = None):
        '''Set position.'''
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def add(self, other_num):
        '''Add to another number.'''
        if isinstance(other_num, Number):
            return Number(self.value + other_num.value)

    def sub(self, other_num):
        '''Subract by another number.'''
        if isinstance(other_num, Number):
            return Number(self.value - other_num.value)

    def mul(self, other_num):
        '''Multiply by another number.'''
        if isinstance(other_num, Number):
            return Number(self.value * other_num.value)

    def div(self, other_num):
        '''Divide by another number.'''
        if isinstance(other_num, Number):
            return Number(self.value / other_num.value)

    def __repr__(self):
        return str(self.value)
