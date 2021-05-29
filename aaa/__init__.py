from .lexer import Lexer
from .parser import Parser

def run(fn, code):
    lexer = Lexer(fn, code)
    tok, error = lexer.make_tokens()
    if error: return error

    # Generate abstract syntax tree.
    parser = Parser(tok)
    ast = parser.parse()

    if ast.error: return ast.error
    return ast.node