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
    print(ng)


if __name__ == '__main__':
    main()

