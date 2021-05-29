# Interpreter
from .types import *
from .token import *

class Interpreter:
    def visit(self, node):
        '''Process the node and it's children.'''
        name = f'visit_{type(node).__name__}'
        method = getattr(self, name)
        return method(node)

    def visit_NumberNode(self, node):
        '''Visit number node.'''
        return Number(node.tok.value).set_pos(node.pos_start, node.pos_end)

    def visit_BinOpNode(self, node):
        '''Visit binary operation node and it's children.'''
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op_tok.type == TT_PLUS:
            res = left.add(right)
        elif node.op_tok.type == TT_MINUS:
            res = left.sub(right)
        elif node.op_tok.type == TT_MUL:
            res = left.mul(right)
        elif node.op_tok.type == TT_DIV:
            res = left.div(right)

        return res.set_pos(node.pos_start, node.pos_end)

    def visit_UnaryOpNode(self, node):
        '''Visit unary operation node and it's children.'''
        num = self.visit(node.node)

        if node.op_tok.type == TT_MINUS:
            num = num.mul(Number(-1))

        return num.set_pos(node.pos_start, node.pos_end)