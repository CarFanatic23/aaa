# Error

class Error:
    def __init__(self, pos_start, pos_end, name, details):
        '''Base class for all errors.'''
        self.name = name
        self.details = details
        self.pos_start = pos_start
        self.pos_end = pos_end

    def __repr__(self):
        return f'''File "{self.pos_start.fn}", Line {self.pos_start.ln + 1}
    {self.name}: {self.details}'''

# Illegal character error
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        '''Illegal character error.'''
        super().__init__(pos_start, pos_end, 'IllegalCharError', details)

# Invalid syntax error
class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details):
        '''Illegal syntax error.'''
        super().__init__(pos_start, pos_end, 'InvalidSyntaxError', details)

# Runtime error
class RuntimeError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        '''Runtime error.'''
        self.context = context
        super().__init__(pos_start, pos_end, 'RuntimeError', details)
    
    def gen_traceback(self):
        res = 'Traceback (most recent call last):\n'
        pos = self.pos_start
        context = self.context

        while context:
            res += f'    File "{pos.fn}", Line {pos.ln + 1}, in {context.display_name}\n'
            pos = context.parent_en_pos
            context = context.parent

        return res

    def __repr__(self):
        return f'{self.gen_traceback()}{self.name}: {self.details}'