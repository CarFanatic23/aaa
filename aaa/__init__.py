from .lexer import Lexer

def run(fn, code):
    lexer = Lexer(fn, code)
    return lexer.make_tokens()