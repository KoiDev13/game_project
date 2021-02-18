import random

while True:
    player = input('Please enter your choice (rock, paper, scissors): ')
    possibility = ['rock', 'paper', 'scissors']
    computer = random.choice(possibility)
    print(f'\nYou chose {player} \nThe computer chose {computer}')

    if player == computer:
        print(f"Both players selected {player}. It's a tie!") #f-String, put the variable into string
    elif player == 'rock':
        if computer == 'scissors':
            print('Rock smashes scissors! You won! Horray!')
        else:
            print('Paper covers rock! You lose.')
    elif player == 'scissors':
        if computer == 'paper':
            print('Scissors cuts paper! You won! Horray!')
        else:
            print('Rock smashes scissors! You lose.')
    elif player == 'paper':
        if computer == 'rock':
            print('Paper covers rock! You won! Horray!')
        else:
            print('Scissors cuts paper! You lose.')
    play_again = input('You wana play again? (y/n):')
    if play_again.lower() != "y":
        break