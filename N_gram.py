#
# Eli Saracino
# esaracin@bu.edu
#
# A class to implement a very simple n-gram algorithm,
# which looks at the previous n moves, and simply returns the
# most frequently used move. This move will be countered by the AI
# while playing the game.
#

import random

class N_gram:

    def __init__(self, n):
        self.n = n
    
    def getMostFrequent(self, prev_moves):
        num_moves = len(prev_moves)
        if num_moves == 0:
            return random.choice(['r', 'p', 's'])

        return 0

