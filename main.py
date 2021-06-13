import random

game_objects = ['rock', 'paper', 'scissor']
player_name = input('Enter your name: ')
rounds = int(input('Enter the number of rounds: '))
reply_yes = ['y', 'yes', 'yeah', 'yup', 'yep']

def roundsAreZero():
    warning = print('You cannot enter 0 or negetive integers. The minimum number of rounds is 1')
    return warning

if rounds <= 0:
    roundsAreZero()

elif rounds >= 1:
    pass

def gameLogic():
    player_points = 0
    computer_points = 0
    for i in range(rounds):
        player_move = input('rock, paper or scissor? ').lower()
        computer_move = random.choice(game_objects)
        if player_move == computer_move:
            print(computer_move)
            print('Its a tie!')
            print(f"computer's points: {computer_points}")
            print(f"{player_name}'s points: {player_points}")

        elif player_move == 'rock' and computer_move == 'paper':
            print(computer_move)
            print('computer won!')
            computer_points += 1
            print(f"{player_name}'s points: {player_points}")
            print(f"computer's points: {computer_points}")

        elif player_move == 'rock' and computer_move == 'scissor':
            print(computer_move)
            print(f"{player_name} won!!")
            player_points += 1
            print(f"user's points: {player_points}")

        elif player_move == 'paper' and computer_move == 'rock':
            print(computer_move)
            print(f"{player_name} won!!")
            player_points += 1
            print(f"user's points: {player_points}")

        elif player_move == 'paper' and computer_move == 'scissor':
            print(computer_move)
            print('computer won!')
            computer_points += 1
            print(f"{player_name}'s points: {player_points}")
            print(f"computer's points: {computer_points}")

        elif player_move == 'scissor' and computer_move == 'paper':
            print(computer_move)
            print(f"{player_name} won!!")
            player_points += 1
            print(f"user's points: {player_points}")

        elif player_move == 'scissor' and computer_move == 'rock':
            print(computer_move)
            print('computer won!')
            computer_points += 1
            print(f"{player_name}'s points: {player_points}")
            print(f"computer's points: {computer_points}")

        elif player_move == 'end':
            if player_points > computer_points:
                print(f"{player_name} is the winner")
                print(f"{player_name}'s points: {player_points}")
                print(f"computer's points: {computer_points}")

            elif player_points < computer_points:
                print('computer won!')
                print(f"{player_name}'s points: {player_points}")
                print(f"computer's points: {computer_points}")

            else:
                print('Match Tied!!')
                print(f"{player_name}'s points: {player_points}")
                print(f"computer's points: {computer_points}")
            break

        else:
            print('Invalid Input')
            user_playAgain = input('Wanna play again? ').lower()
            if user_playAgain in reply_yes:
                gameLogic()

            else:
                break

if rounds >= 1:
    gameLogic()
