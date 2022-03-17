from tests.flow.flo import Flo
from game_of_greed.game_2 import Game


def test_one_and_done():
    Game.rolled_dices = [[4, 4, 5, 2, 3, 1]]
    Flo.test("../tests/flow/one_and_done.sim.txt")
