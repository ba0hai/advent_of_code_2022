from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class RPSResult(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

class Result(Enum):
    X = RPSResult.LOSE
    Y = RPSResult.DRAW
    Z = RPSResult.WIN

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

def what_to_play(opponent, result):
    if result.value == RPSResult.WIN:
        if opponent.value == RPS.ROCK:
            return RPS.PAPER
        elif opponent.value == RPS.SCISSORS:
            return RPS.ROCK
        elif opponent.value == RPS.PAPER:
            return RPS.SCISSORS
    else:
        if opponent.value == RPS.ROCK:
            return RPS.SCISSORS
        elif opponent.value == RPS.SCISSORS:
            return RPS.PAPER
        elif opponent.value == RPS.PAPER:
            return RPS.ROCK

def solve():
    input = get_input()
    total_score = 0
    for val in input:
        score = 0
        play1 = Player1Play[val[0]]
        result = Result[val[1]]
        if result.value == RPSResult.DRAW:
            score = 3 + play1.value.value
        elif result.value == RPSResult.WIN:
            to_play = what_to_play(play1, result)
            score = 6 + to_play.value
        elif result.value == RPSResult.LOSE:
            to_play = what_to_play(play1, result)
            score = to_play.value
        total_score += (score * input[val])
    return total_score

def main():
    print("Day 2 answer here")
    print(solve())

main()