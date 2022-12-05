from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Player1Play(Enum):
    A = RPS.ROCK
    B = RPS.PAPER
    C = RPS.SCISSORS

class Player2Play(Enum):
    X = RPS.ROCK
    Y = RPS.PAPER
    Z = RPS.SCISSORS

def game_result(play1, play2):
    if (play1 == RPS.ROCK and play2 == RPS.ROCK) or (play1 == RPS.SCISSORS and play2 == RPS.SCISSORS) or (play1 == RPS.PAPER and play2 == RPS.PAPER):
        return 0
    elif play1 == RPS.ROCK and play2 == RPS.PAPER:
        return 1
    elif play1 == RPS.ROCK and play2 == RPS.SCISSORS:
        return -1
    elif play1 == RPS.PAPER and play2 == RPS.ROCK:
        return -1
    elif play1 == RPS.PAPER and play2 == RPS.SCISSORS:
        return 1
    elif play1 == RPS.SCISSORS and play2 == RPS.ROCK:
        return 1
    elif play1 == RPS.SCISSORS and play2 == RPS.PAPER:
        return -1

def get_input():
    with open('input') as f:
        lines = {}
        vals = f.readlines()
        for val in vals:
            val_len = len(val)
            val = val[:val_len-1]
            split_val = val.split(" ")
            if lines.get((split_val[0], split_val[1]), -1) == -1:
                lines[(split_val[0], split_val[1])] = 1
            else:
                lines[(split_val[0], split_val[1])] += 1

    return lines

def solve():
    input = get_input()
    total_score = 0
    for val in input:
        score = 0
        play1 = Player1Play[val[0]]
        play2 = Player2Play[val[1]]
        result = game_result(play1.value, play2.value)
        if result == 0:
            score = play2.value.value + 3
        elif result == 1:
            score = play2.value.value + 6
        elif result == -1:
            score = play2.value.value
        print((play1, play2), result, score)
        total_score += (score * input[val])
    return total_score

def main():
    print("Day 2 answer here")
    print(solve())

main()