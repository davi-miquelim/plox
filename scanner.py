import TokenType 
import Token
import Lox

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1


    def scan_tokens(self):
        while !(self.is_at_end()):
            self.start = self.current
            scan_token()

        self.tokens.push(Token(TokenType.EOF, "", null, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_token(self):
        c = self.advance()

        match c:
            case '(':
                self.add_token(TokenType.LEFT_PAREN)
            case ')':
                self.add_token(TokenType.RIGHT_PAREN)
            case '{': 
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token(TokenType.COMMA)
            case '.':
                self.add_token(TokenType.DOT)
            case '-':
                self.add_token(TokenType.MINUS)
            case '+':
                self.add_token(TokenType.PLUS)
            case ';':
                self.add_token(TokenType.SEMICOLON)
            case '*':
                self.add_token(TokenType.STAR)
            case _:
                Lox.error(self.line, "Unexpected character.")

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def add_token(self, token_type, literal = Null):
        text = self.source.substring[self.start, self.current]
        self.tokens.push(Token(token_type, text, literal, self.line)) 

