#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

"""
Rock, Paper, Scissors game based on AOC day 2.

This is a 3 round game. At the end of each round
the opponent who wins the round scores 6 points,
a draw is 3 points, loss is 0. Additionally, in
each round, a player is awarded additional points
based on the shape (rock, paper, scissors) they
play regardless whether they win/lose or draw the
round. Rock = 1, paper = 2, and scissors = 3
"""

from enum import Enum
from typing import List

class Points(Enum):
    """
    These are the default points awarded for
    the Shapes played by the player (ROCK, PAPER,
    SCISSORS), and also the points awarded if a
    player WIN or DRAW.
    """
    ROCK     = 1
    PAPER    = 2
    SCISSORS = 3
    DRAW     = 3
    WIN      = 6

class Shapes(Enum):
    """
    ROCK, PAPER, SCISSORS are the only shapes players
    can play in a round.
    """
    ROCK     = "rock"
    PAPER    = "paper"
    SCISSORS = "scissors"

class Outcome(Enum):
    """
    These are the game outcomes. Players can either
    WIN, LOSE or DRAW.
    """
    DRAW = "draw"
    WIN  = "win"
    LOSE = "lose"

def default_point(shape_played) -> int:
    """
    Returns the default point based on the shape the
    player has chosen that round. This point is given
    regardless of whether the player wins/loses/or draws
    the round.
    """
    match shape_played:
        case Shapes.ROCK:
            return Points.ROCK.value
        case Shapes.PAPER:
            return Points.PAPER.value
        case _:
            return Points.SCISSORS.value

def rps_game(p1: Shapes, p2: Shapes) -> Outcome:
    """
    Rock, Paper, Scissors game logic
    Rock beats scissors, scissors beats paper,
    and paper beats rock. The returned Outcome (Enum) outcome
    is based from the perspective of player 1.
    """
    if p1 == p2:
        return Outcome.DRAW
    if p1 == Shapes.ROCK and p2 == Shapes.SCISSORS:
        return Outcome.WIN
    if p1 == Shapes.SCISSORS and p2 == Shapes.PAPER:
        return Outcome.WIN
    if p1 == Shapes.PAPER and p2 == Shapes.ROCK:
        return Outcome.WIN
    return Outcome.LOSE

def test() -> None:
    # TODO: Put test() in its own test file.
    assert rps_game(Shapes.ROCK, Shapes.SCISSORS)  ==  Outcome.WIN
    assert rps_game(Shapes.PAPER, Shapes.ROCK)     ==  Outcome.WIN
    assert rps_game(Shapes.SCISSORS, Shapes.PAPER) ==  Outcome.WIN

    assert rps_game(Shapes.SCISSORS, Shapes.ROCK)  ==  Outcome.LOSE
    assert rps_game(Shapes.ROCK, Shapes.PAPER)     ==  Outcome.LOSE
    assert rps_game(Shapes.PAPER, Shapes.SCISSORS) ==  Outcome.LOSE

    assert rps_game(Shapes.ROCK, Shapes.ROCK)         ==  Outcome.DRAW
    assert rps_game(Shapes.PAPER, Shapes.PAPER)       ==  Outcome.DRAW
    assert rps_game(Shapes.SCISSORS, Shapes.SCISSORS) ==  Outcome.DRAW

def main() -> None:
    A = X = Shapes.ROCK
    B = Y = Shapes.PAPER
    C = Z = Shapes.SCISSORS

    opp_plays: List[Shapes] = [A, B, C]
    my_plays:  List[Shapes] = [Y, X, Z]

    opp_score = 0
    my_score = 0

    i = 0
    while i < len(my_plays):

        my_score  += default_point(my_plays[i])
        opp_score += default_point(opp_plays[i])

        curr_round = rps_game(my_plays[i], opp_plays[i])

        if curr_round == Outcome.WIN:
            my_score += Points.WIN.value
        elif curr_round == Outcome.LOSE:
            opp_score += Points.WIN.value
        else:
            my_score += Points.DRAW.value
            opp_score += Points.DRAW.value

        i+=1

    print(f"Final Scores: me => {my_score} VS. opponent => {opp_score}")

if __name__ == "__main__":
    test() #TODO: Put test() in its own test file.
    main()
