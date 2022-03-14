from random import randint
from collections import Counter


class GameLogic:
    def roll_dice(n=6):
        return tuple([randint(1, 6) for _ in range(n)])

    @staticmethod
    def calculate_score(dices):
        rules = {
            1: {1: 100, 2: 200, 3: 1000, 4: 2000, 5: 3000, 6: 4000},
            2: {1: 0, 2: 0, 3: 200, 4: 400, 5: 600, 6: 800},
            3: {1: 0, 2: 0, 3: 300, 4: 600, 5: 900, 6: 1200},
            4: {1: 0, 2: 0, 3: 400, 4: 800, 5: 1200, 6: 1600},
            5: {1: 50, 2: 100, 3: 500, 4: 1000, 5: 1500, 6: 2000},
            6: {1: 0, 2: 0, 3: 600, 4: 1200, 5: 1800, 6: 2400},
            7: 1500,
            8: 1500,
        }
        counts = Counter(dices)
        result = counts.most_common()
        score = 0

        if len(dices) == 0:
            return 0
        if len(counts) == 6:
            return rules[7]

        if len(dices) == 6 and len(result) == 3 and result[0][1] == 2:
            return rules[8]

        for i in result:
            score += rules[i[0]][i[1]]
        return score


if __name__ == "__main__":
    game_logic = GameLogic()
    straight = (1, 2, 3, 4, 5, 6)
    three_fives = (5, 5, 5, 2, 2, 3)
    single_five = (5,)
    three_pairs = (2, 2, 1, 1, 6, 6)
    x = game_logic.calculate_score(three_fives)
    print(x)
