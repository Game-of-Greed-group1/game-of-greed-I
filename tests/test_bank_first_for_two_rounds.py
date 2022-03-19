from tests.flow.flo import Flo
from game_of_greed.game_2 import Game


def test_one_and_done():
    Game.rolled_dices = [[1, 4, 4, 6, 1, 6], [3, 4, 6, 1, 3, 6], [3, 4, 1, 4, 3, 5]]
    Flo.test("../tests/flow/bank_first_for_two_rounds.sim.txt")
