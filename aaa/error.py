# Error

class Error:
    def __init__(self, pos_start, pos_end, name, details):
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