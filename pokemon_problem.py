class Pokemon:
    pokedex = ["Pikachu", "Jigglypuff", "Squirtle",
               "Ditto", "Onyx", "Charizard", "Clefairy", "Snorlax"]

    def __init__(self, name, health, damage) -> None:
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, foe_pokemon):
        foe_pokemon.health -= self.damage

    def check_if_fainted(self):
        isFainted = False
        if self.health <= 0:
            isFainted = True
        else:
            isFainted = False
        return isFainted

    @classmethod
    def print_pokedex(cls):
        for pokemon in cls.pokedex:
            print(pokemon)

    # @classmethod
    # def check_if_fainted(cls, pokemon):
    #     if pokemon.health <= 0:
    #         return True


class PokemonTrainer:
    def __init__(self, name) -> None:
        self.name = name
        self.pokemons = []
        # if we have time, gender , etc.

    def add_pokemon(self, pokemon_to_add):
        if len(self.pokemons) > 6:
            print("cannot add!")
            return

        self.pokemons.append(pokemon_to_add)

    def battle(self, other_trainer):
        my_pokemon = self.pokemons[0]
        foe_pokemon = other_trainer.pokemons[0]

        if my_pokemon.check_if_fainted():
            print("Your pokemon is fainted")
            return
        elif foe_pokemon.check_if_fainted():
            print("Your opponent's pokemon is fainted")
            return

        my_pokemon.attack(foe_pokemon)
        if foe_pokemon.check_if_fainted():
            print("You have defeated the opponent!")
        else:
            print("Haven't defeated opponent yet")


class GymLeader(PokemonTrainer):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def get_badge(self):
        if self.pokemons[0].check_if_fainted():
            print(f"here's the {self.type} badge!")
        else:
            print("you havent defeated me yet!")

# Pokemon.print_pokedex()


ash = PokemonTrainer("Ash")
brock = PokemonTrainer("Brock")

pikachu = Pokemon(health=5, name="Pikachu", damage=5)
psyduck = Pokemon("Psyduck", 6, 4)

ash.add_pokemon(pikachu)
brock.add_pokemon(psyduck)

ash.battle(brock)
ash.battle(brock)

print()
misty = GymLeader("Misty", "water")
print(misty.type)
misty.get_badge()
