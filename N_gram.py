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
    
    def get_most_frequent(self, prev_moves):
        num_moves = len(prev_moves)

        # Get the last n-moves
        last_moves = prev_moves[-self.n:]

        if num_moves == []: # Error check for first case, throw choice randomly
            return random.choice(['r', 'p', 's'])
        else:
            counts = {'r': 0, 'p': 0, 's': 0}
            for move in last_moves:
                counts[move] += 1

            most_freq = max(counts.values())
            options = [choice for choice in counts if counts[choice] == most_freq]

            return random.choice(options)

