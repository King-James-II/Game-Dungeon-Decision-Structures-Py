# Fantasy Dungeon: Dark Secrets

"""
This Python program simulates a fantasy dungeon adventure where the player must navigate through treacherous paths,
encounter dangerous creatures, and uncover hidden secrets. It showcases decision structures including boolean expressions
and operators, comparison operators, logical operators, if statements, nested if statements, data validation, and
exception handling.
"""

import random

def explore_dungeon():
    print("You enter the dark and eerie dungeon...")
    print("As you venture deeper, you encounter a fork in the path.")

    # Data validation to ensure the player chooses a valid option
    while True:
        direction = input("Do you go left or right? (left/right): ").lower()
        if direction == "left" or direction == "right":
            break
        else:
            print("Invalid input. Please enter 'left' or 'right'.")

    if direction == "left":
        print("You chose to go left and encounter a sleeping dragon!")
        engage_dragon()
    else:
        print("You chose to go right and find a hidden treasure chest!")
        discover_treasure()

def engage_dragon():
    print("The dragon awakens and roars furiously!")
    print("You must decide whether to fight or flee.")

    while True:
        decision = input("Do you fight or flee? (fight/flee): ").lower()
        if decision == "fight":
            print("You bravely stand your ground and prepare to battle the dragon!")
            battle_dragon()
            break
        elif decision == "flee":
            print("You decide to flee the dragon and escape the dungeon.")
            break
        else:
            print("Invalid input. Please enter 'fight' or 'flee'.")

def battle_dragon():
    dragon_health = random.randint(50, 100)
    player_health = 100
    print("The battle begins!")
    while dragon_health > 0 and player_health > 0:
        # Simulate combat with random damage
        dragon_damage = random.randint(5, 15)
        player_damage = random.randint(10, 20)
        dragon_health -= player_damage
        player_health -= dragon_damage
        print(f"You attack the dragon, dealing {player_damage} damage.")
        print(f"The dragon retaliates, dealing {dragon_damage} damage to you.")
        print(f"Dragon's Health: {dragon_health}, Your Health: {player_health}")

    if player_health > 0:
        print("Congratulations! You defeated the dragon and emerged victorious!")
    else:
        print("You were defeated by the dragon. Game over.")

def discover_treasure():
    print("You discover a hidden treasure chest filled with gold coins and magical artifacts!")
    print("As you reach for the treasure, a trap is triggered!")
    print("You must solve a riddle to disarm the trap and claim the treasure.")

    riddle = "What is always in front of you but can’t be seen?"
    answer = "the future"

    while True:
        user_answer = input("Enter your answer to the riddle: ").lower()
        if user_answer == "answer":
            print("Congratulations! You solved the riddle and safely obtained the treasure!")
            break
        else:
            print("Incorrect answer. Try again!")

# Main program entry point
if __name__ == "__main__":
    explore_dungeon()
