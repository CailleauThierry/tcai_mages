# AUTOGENERATED! DO NOT EDIT! File to edit: 01_game.ipynb (unless otherwise specified).

__all__ = ['init_player', 'combat', 'COMBAT_OPTIONS', 'game_loop']

# Cell
def init_player():
    "Initializes a player, `Mage`, with the user's speciality and name"
    print(f"Hi there, what is your speciality? {Ability.ability_types}")
    while True:
        ability_types = input()
        if ability_types in Ability.ability_types:
            break
        else:
            print(f"Invalid ability choice, What is your Speciality? {Ability.ability_types}")
    name = input("What is your name, mage?")
    return Mage(name, 100, Ability(10, ability_types))

# Cell
COMBAT_OPTIONS = ["attack"]

def combat(player, boss):
    "Performs a combat with a player, `Mage`, which as generated with the `init_player` function, and a `Demon`"
    print("Combat has begun!")
    while True:
        print(player)
        print(boss)
        print(f"What do you want to do? {COMBAT_OPTIONS}")
        player_move = input()
        if player_move not in COMBAT_OPTIONS:
            print("Not an option, you lose a move!")
        else:
            if player_move == "attack":
                player.attack(boss)
                if boss.current_health <= 0:
                    return player
        boss.attack(player)
        if player.current_health <= 0:
            return boss

# Cell
def game_loop(player, n = 5):
    for i in range(1, n + 1):
        boss = Demon("Gary", 50 * i)
        print(f"A demon name {boss.name}) appeared! They seem to have a chip on their shoulder and want to fight you.")
        winner = combat(player, boss)
        if winner == player:
            print(f"Well done, you beat {boss.name} and leveled up to {i + 1}! ")
            player.level_up()
        else:
            print(f"You have fallen to {boss.name}. Game Over!")
            break
    if i == n:
        print(f"Congratulations, you've defeated all the bosses and won the game. {player.name}'s name shall go down in history!")