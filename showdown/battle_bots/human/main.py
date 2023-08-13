from showdown.battle import Battle

from ..helpers import format_decision
from ..helpers import pick_safest_move_from_battles


class BattleBot(Battle):
    def __init__(self, *args, **kwargs):
        super(BattleBot, self).__init__(*args, **kwargs)

    def find_best_move(self):
        battles = self.prepare_battles(join_moves_together=True)

        for i, b in enumerate(battles):
            user_options, opponent_options = b.get_all_options()
        
        print(opponent_options)
        move = "NOMOVE"
        if move not in user_options:
            move = input(f"Choose move: {user_options}\n")
        return format_decision(self, move)
