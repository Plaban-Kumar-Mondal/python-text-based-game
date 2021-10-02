# This is a fun little project me and my friends are doing
# A little text based console rpg game

import random
from Humanoid import Humanoid


level = 1
player = Humanoid(100, 12)


def enter_a_room(player, max_enemy_num):
    player_input = ""
    ene_current_hel = 0
    # enemies = list()
    # enemy_count = random.randint(1, max_enemy_num)
    # for i in range(enemy_count):
    #     enemies.append(Humanoid(20, 5))

    enemy_one = Humanoid(20, 5)
    ene_current_hel = enemy_one.health

    # enem_alert_msg = (
    #     f"Oh no! {enemy_count} enemies have appeared!"
    #     if enemy_count > 1
    #     else f"Oh no! {enemy_count} enemy have appeared!"
    # )
    print("A enemy has appeared!")
    input("\nPress Enter to continue...\n")
    print(
        "(tutorial) Type 'A' to attack. In first turn you will attack then enemy will attack you."
    )

    player_input = input("\nType your action:\n")
    while ene_current_hel > 0:
        if player_input.upper() == "A":
            ene_current_hel = enemy_one.hurt(player.attack_damage)
            print("You hit hard!")
            print(
                f"Enemy Health: {ene_current_hel}         Player health: {player.current_health}"
            )


# Main Game Loop
while True:
    print(
        """
You heard something and you woke up. But it isn't your bedroom! 
A dark room with a very small window and you were sleeping on the stone floor.
You stand up and walk to the window to see outside. You can see a courtyard and a big wall.
You quickly understand that you're in the old castle. But how did you end up here? Aah headache! You can't remember a thing
        """
    )
    input("\nPress Enter to continue...\n")
    print("You need to get out of this castle")
    input("\nPress Enter to continue...\n")
    print(
        "Now you can see two doors infront of you!! A door on your left and a door on your right."
    )
    input("\nType L to choose left door and R to choose right door\n")

    enter_a_room(player, 3)
