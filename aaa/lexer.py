# Lexer
from .token import *
from .error import IllegalCharError
from .position import Position
import string

class Lexer:
    def __init__(self, fn, code):
        self.code = code
        self.pos = Position(-1, 0, -1, fn, code)
        self.curr = None
        self.fn = fn
        self.advance()

    def advance(self):
        '''Advance to next character.'''
        self.pos.advance()
        self.curr = self.code[self.pos.idx] if self.pos.idx < len(self.code) else None

    def make_tokens(self):
        '''Make tokens for code.'''
        tokens = []

        while self.curr != None:
            if self.curr in ' \t':
                self.advance()
                continue
            elif self.curr in string.digits:
                tokens.append(self.make_number())
                continue
            elif self.curr in string.ascii_letters:
                tokens.append(self.make_id())
                continue
            elif self.curr == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
            elif self.curr == '-':
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
            elif self.curr == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
            elif self.curr == '/':
                tokens.append(Token(TT_DIV, pos_start=self.pos))
            elif self.curr == '^':
                tokens.append(Token(TT_POW, pos_start=self.pos))
            elif self.curr == '=':
                tokens.append(Token(TT_EQ, pos_start=self.pos))
            elif self.curr == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
            elif self.curr == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
            else:
                char = self.curr
                pos_start = self.pos.copy()
                self.advance()
                return None, IllegalCharError(pos_start, self.pos, f'`{char}`')

            self.advance()

        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        '''Makes number.'''
        num = ''
        dots = 0
        pos_start = self.pos.copy()

        while self.curr != None and self.curr in string.digits + '.':
            if self.curr == '.':
                if dots == 1: break
                dots += 1
                num += '.'
            else:
                num += self.curr

            self.advance()

        if dots == 0:
            return Token(TT_INT, int(num), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num), pos_start, self.pos)

    def make_id(self):
        '''Identifier.'''
        id_str = ''
        pos_start = self.pos.copy()
        allowed_chars = string.digits + string.ascii_letters + '_'

        while self.curr != None and self.curr in allowed_chars:
            id_str += self.curr
            self.advance()
            
        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str, pos_start, self.pos)