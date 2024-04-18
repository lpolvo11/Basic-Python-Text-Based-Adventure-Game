import time
import os
import random


class Creature:
    def __init__(self, name, health, clazz):
        self.name = name
        self.health = health
        self.clazz = clazz


class Hero(Creature):
    def __init__(self):
        super().__init__(name="Hero", health=100, clazz="Warrior")


class Enemy(Creature):
    def __init__(self):
        super().__init__(name="Enemy", health=100, clazz="Monster")


def discover():
    print("Exploring...")
    time.sleep(1)
    print("Oh there is a goblin there :")
    time.sleep(2)
    goblin = Enemy()
    while True:
        enemy_appear_choice = input("1) to fight, 2) to run away:   ")
        random_damage = random.randint(0, 50)
        if enemy_appear_choice == "1":
            goblin.health -= random_damage
            if goblin.health <= 0:
                print("you won")
                break
            print(goblin.health)
        elif enemy_appear_choice == "2":
            print("You ran away from the goblin...")
            exit()


def create_character():
    character_name = input("Enter your character's name: ")
    character_clazz = input("Choose your class: (Hunter / Knight / Witcher): ")
    if character_clazz.lower() not in ["hunter", "knight", "witcher"]:
        print("Please Enter a valid character class.")
        exit()
    else:
        time.sleep(1)
        print(f"You are {character_name}, the {character_clazz}")
        return character_name, character_clazz


def main():
    create_character()
    player = Hero()

    while True:
        main_choice = input("Choose what do you want to do: 1) Explore forest, 2) View State, 3)Quit : ")
        if main_choice == "1":
            os.system("cls")
            discover()
        elif main_choice == "2":
            print(f"You are a {player.name}, and your class is a {player.clazz}")
        elif main_choice == "3":
            print("Quiting game...")
            time.sleep(2)
            exit()
        else:
            print("Invalid choice please Try again")


if __name__ == "__main__":
    main()
