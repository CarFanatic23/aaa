# Symbol table

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def get(self, name):
        '''Get variable.'''
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set_var(self, name, value):
        '''Set variable.'''
        self.symbols[name] = value

    def remove(self, name):
        '''Remove variable.'''
        del self.symbols[name]