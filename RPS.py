import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if len(opponent_history) < 3:
        return random.choice(['R', 'P', 'S'])

    # Most common move by opponent
    most_common = max(set(opponent_history), key=opponent_history.count)

    # Counter the opponent's most common move
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}

    return counter[most_common]
