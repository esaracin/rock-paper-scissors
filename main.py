#
# Eli Saracino
# esaracin@bu.edu
#
# This is the driving Python script for our simple 
# AI implementation of Rock, Paper, Scissors.
#
#

from N_gram import *

def main():

    # First, get difficulty from user and create our model
    while True:
        diff = int(input('Please enter your difficulty level (between 1 and 25): '))
        if(diff >= 0 and diff <= 25):
            break

        print('That isn\'t a valid difficulty!')

    ng = N_gram(diff)

    # Start the game
    play_game(ng)


def play_game(ng):
    opp_moves = []
    stats = {'wins': 0, 'loses': 0, 'ties': 0}

    win_dict = {'r': 's', 'p': 'r', 's': 'p'}
    loss_dict = {'r': 'p', 'p': 's', 's': 'r'}

    print('Lets play the game! Please press r for rock, p for paper, or s for scissors! (q to quit)')
    print()
    while True:
        opp_move = str(input('What is your move? '))
        if(opp_move == 'q'):
            break

        ai_move = loss_dict[ng.get_most_frequent(opp_moves)]


        if win_dict[opp_move] == ai_move:
            print('You win!')
            stats['wins'] += 1
        elif opp_move == ai_move:
            print('It\'s a tie!')
            stats['ties'] += 1
        else:
            print('You lose!')
            stats['loses'] += 1


    print('You had ')

if __name__ == '__main__':
    main()

