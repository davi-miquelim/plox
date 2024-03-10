import sys

class Lox:
    def __init__(self, args):
        self.had_error = False

        if len(args) > 1:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(args) == 1:
            run_file(args[0])
        else:
            run_prompt()

    def run_file(self, path):
        file = open(path)
        run(file)

        if self.had_error == True:
            sys.exit(65)

    def run_prompt(self):
        while True:
            user_input = input("> ");

            if user_input == Null:
                break;

            run(user_input);
            self.had_error = False

    def run(self, source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    def error(self, line, message):
        report(line, "", message)

    def report(self, line, where, message):
        print(f'[{line}] Error {where}: {message}')
        self.had_error = True

