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
        self.pos.advance(self.curr)
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
            elif self.curr == '+':
                tokens.append(Token(TT_PLUS))
            elif self.curr == '-':
                tokens.append(Token(TT_MINUS))
            elif self.curr == '*':
                tokens.append(Token(TT_MUL))
            elif self.curr == '/':
                tokens.append(Token(TT_DIV))
            elif self.curr == '(':
                tokens.append(Token(TT_LPAREN))
            elif self.curr == ')':
                tokens.append(Token(TT_RPAREN))
            else:
                char = self.curr
                pos_start = self.pos.copy()
                self.advance()
                return IllegalCharError(pos_start, self.pos, f'`{char}`')

            self.advance()

        return tokens

    def make_number(self):
        '''Makes number.'''
        num = ''
        dots = 0

        while self.curr != None and self.curr in string.digits + '.':
            if self.curr == '.':
                if dots == 1: break
                dots += 1
                num += '.'
            else:
                num += self.curr

            self.advance()

        if dots == 0:
            return Token(TT_INT, int(num))
        else:
            return Token(TT_FLOAT, float(num))