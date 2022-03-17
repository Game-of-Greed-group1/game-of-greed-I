from tests.flow.flo import Flo
from game_of_greed.game_2 import Game


def test_one_and_done():
    Game.rolled_dices = [[2, 3, 1, 3, 1, 2], [4, 1, 4, 4, 3, 4], [3, 2, 3, 2, 1, 4]]
    Flo.test("../tests/flow/hot_dice.txt")
    pass
