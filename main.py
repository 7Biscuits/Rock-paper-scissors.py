import random

random_result = ["Rock", "Paper", "Scissor"]
user_end = ["end", "End", "END", "finish", "Finish", "FINISH"]
user_yes = ["Yes", "yes", "YES", "Yeah", "Ofcource", "Yep", "yep", "YEP"]
user_no = ["No", "no", "NO", "Nope", "NOPE", "nope", "never", "Never", "NEVER"]

def main():
    user_points = 0
    computer_points = 0

    while True:
        user_ask = input("Rock, Paper or Scissor? ")
        result = random.choice(random_result)
        
        if user_ask == result:
            print("Tie!!")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Paper" and result == "Rock":
            print("You won!")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            user_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Paper" and result == "Scissor":
            print("You lost")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            computer_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Rock" and result == "Paper":
            print("You lost")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            computer_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Rock" and result == "Scissor":
            print("You won!!")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            user_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Scissor" and result == "Rock":
            print("You lost")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            computer_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask == "Scissor" and result == "Paper":
            print("You won!")
            print("Your move: " + user_ask)
            print("Computer's move: " + result)
            user_points += 1
            print("Your points: ", user_points)
            print("Computer's points: ", computer_points)

        elif user_ask in user_end:
            if user_points > computer_points:
                print("You have won against computer")
                print("Your points: ", user_points)
                print("Computer's points: " + computer_points)

            elif user_points < computer_points:
                print("You have lost against computer")
                print("Your points: ", user_points)
                print("Computer's points: " + computer_points)

            else:
                print("Its a tie between computer and You")
                print("Your points: ", user_points)
                print("Computer's points: " + computer_points)
            break

        else:
            print("Invalid Input")
            user_error_ask = input("Will you like to try again? ")

            if user_error_ask in user_yes:
                return main()
            
            elif user_error_ask in user_no:
                break
            
main()
