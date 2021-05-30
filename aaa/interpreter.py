# Interpreter
from .types import *
from .token import *
from .rt_result import RuntimeResult

class Interpreter:
    def visit(self, node, context):
        '''Process the node and it's children.'''
        name = f'visit_{type(node).__name__}'
        method = getattr(self, name)
        return method(node, context)

    def visit_NumberNode(self, node, context):
        '''Visit number node.'''
        return RuntimeResult().success(
            Number(node.tok.value).set_context(
                context
            ).set_pos(node.pos_start, node.pos_end)
        )

    def visit_BinOpNode(self, node, context):
        '''Visit binary operation node and it's children.'''
        res = RuntimeResult()
        left = res.register(self.visit(node.left, context))
        if res.error: return res
        right = res.register(self.visit(node.right, context))
        if res.error: return res

        err = None
        if node.op_tok.type == TT_PLUS:
            result = left.add(right)
        elif node.op_tok.type == TT_MINUS:
            result = left.sub(right)
        elif node.op_tok.type == TT_MUL:
            result = left.mul(right)
        elif node.op_tok.type == TT_DIV:
            result, err = left.div(right)

        if err: return res.failure(err)
        return res.success(
            result.set_pos(node.pos_start, node.pos_end)
        )

    def visit_UnaryOpNode(self, node, context):
        '''Visit unary operation node and it's children.'''
        res = RuntimeResult()
        num = res.register(self.visit(node.node, context))
        if res.error: return res

        err = None
        if node.op_tok.type == TT_MINUS:
            num, err = num.mul(Number(-1))

        if err: return res.failure(err)
        return res.success(
            num.set_pos(node.pos_start, node.pos_end)
        )