import random

random_result = ["Rock", "Paper", "Scissor"]
user_end = ["end", "End", "END"]

def main():
    while True:
        user_ask = input("Rock, Paper or Scissor? ")
        result = random.choice(random_result)
        
        if user_ask == result:
            print("Tie!!")

        elif user_ask == "Paper" and result == "Rock":
            print("You won!")

        elif user_ask == "Paper" and result == "Scissor":
            print("You lost")

        elif user_ask == "Rock" and result == "Paper":
            print("You lost")

        elif user_ask == "Rock" and result == "Scissor":
            print("You won!!")

        elif user_ask == "Scissor" and result == "Rock":
            print("You lost")

        elif user_ask == "Scissor" and result == "Paper":
            print("You won!")

        elif user_ask in user_end:
            break
        
        else:
            print("Invalid Input")
            return main()
            
main()
