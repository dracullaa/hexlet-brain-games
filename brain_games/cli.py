import prompt

def cli(name):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')