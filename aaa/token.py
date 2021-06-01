# Token

TT_INT        = 'INT'
TT_FLOAT      = 'FLOAT'
TT_PLUS       = 'PLUS'
TT_MINUS      = 'MINUS'
TT_MUL        = 'MUL'
TT_DIV        = 'DIV'
TT_POW        = 'POW'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD    = 'KEYWORD'
TT_EQ         = 'EQ'
TT_LPAREN     = 'LPAREN'
TT_RPAREN     = 'RPAREN'
TT_EOF        = 'EOF'

KEYWORDS = [
    'set'
]

class Token:
    def __init__(self, type_, value = None, pos_start = None, pos_end = None):
        '''Tokens.'''
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end

    def equals(self, tok_type, value):
        '''Check if token type and value is equal to parameters.'''
        return self.type == tok_type and self.value == value

    def __repr__(self):
        return f'{self.type}:{self.value}' if self.value != None else f'{self.type}'