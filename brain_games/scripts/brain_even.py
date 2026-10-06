import random
from brain_games.scripts.brain_games import main as welcome_user

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return
    
    print(f"Congratulations, {name}!")
