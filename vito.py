from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(33)
        self.spend_attack(33)
        self.spend_defence(34)
        self.add_move(Patada())

        self.set_type(Type.EARTH)

    def get_name(self):
        return "Vito"

    def choose_move(self, enemy):
        return self.get_move_by_name("Earth")

class Patada(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Earth"
