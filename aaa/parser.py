# Parser
from .nodes import *
from .token import *
from .error import InvalidSyntaxError
from .parse_result import ParseResult

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def parse(self):
        res = self.expr()
        if not res.error and self.curr.type != TT_EOF:
            return res.failure(InvalidSyntaxError(
                self.curr.pos_start,
                self.curr.pos_end,
                "Expected '+', '-', '*' or '/'.")
            )

        return res

    def advance(self):
        '''Advance to next token.'''
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.curr = self.tokens[self.tok_idx]

        return self.curr

    def factor(self):
        '''Factor.'''
        res = ParseResult()
        tok = self.curr

        if tok.type in [TT_INT, TT_FLOAT]:
            res.register(self.advance())
            return res.success(NumberNode(tok))

        return res.failure(InvalidSyntaxError(tok.pos_start, tok.pos_end, 'Expected int or float.'))

    def term(self):
        '''Term.'''
        return self.bin_op(self.factor, [TT_MUL, TT_DIV])

    def expr(self):
        '''Expression.'''
        return self.bin_op(self.term, [TT_PLUS, TT_MINUS])

    def bin_op(self, func, op_toks):
        '''Binary operation.'''
        res = ParseResult()
        left = res.register(func())
        if res.error: return res

        while self.curr.type in op_toks:
            op_tok = self.curr
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)