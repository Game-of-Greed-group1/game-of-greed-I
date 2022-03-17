from tests.flow.flo import Flo
from game_of_greed.game_2 import Game


def test_one_and_done():
    Game.rolled_dices = [[5, 2, 3, 4, 6, 6], [6, 5, 1, 6, 6, 6]]
    Flo.test("../tests/flow/bank_one_roll_then_quit.sim.txt")
    pass
