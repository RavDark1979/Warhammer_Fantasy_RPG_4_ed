"""
simple program to roll the opposed test for Warhammer 4.0 Fantasy RPG
set the skill of the attacker
set the skill of the defender
roll for the attacker
roll for the defender
check for crits
compare results
determine the output
again?
"""


def opposed_roll():
    # definitions and inputs
    import random

    doubles = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    attacker_skill_value = int(input("Enter the attacker's skill value: "))
    defender_skill_value = int(input("Enter the defender's skill value: "))

    # roll
    attacker_roll = random.randint(1, 100)
    print(f'The attacker rolled: {attacker_roll}')

    defender_roll = random.randint(11, 11)
    print(f'The defender rolled: {defender_roll}')

    # rules
    if attacker_roll > attacker_skill_value and attacker_roll in doubles:
        print("Fumble effect on the attacker!")
    elif attacker_roll < attacker_skill_value and attacker_roll in doubles:
        print("Critical hit made by the attacker!")
    elif attacker_roll in range(96, 100):
        print("Automatic failure of the attacker!")
    elif attacker_roll in range(1, 5):
        print("Automatic success of the attacker!")

    if defender_roll > defender_skill_value and defender_roll in doubles:
        print("Critical failure defender!")
    elif defender_roll < defender_skill_value and defender_roll in doubles:
        print("Critical hit made by the defender!")
    elif defender_roll in range(96, 100):
        print("Automatic failure of the defender!")
    elif defender_roll in range(1, 5):
        print("Automatic success of the defender!")

    # determining success levels
    success_level_attacker = (attacker_skill_value // 10) - (attacker_roll // 10)
    ten_value_attacker_positive = (str(success_level_attacker)[0])

    if int(success_level_attacker) < 0:
        print(f'Attacker success levels is: {success_level_attacker}')
    elif ten_value_attacker_positive == 0:
        ten_value_attacker_positive = 1
        print(f'Attacker success level is: {int(ten_value_attacker_positive) // 10}')
    else:
        print(f'Attacker success levels is: {success_level_attacker}')

    success_level_defender = (int(defender_skill_value // 10) - (defender_roll // 10))
    ten_value_defender_positive = (str(success_level_defender)[0])

    if int(success_level_defender) < 0:
        print(f'Defender success levels is: {success_level_defender}')

    elif ten_value_defender_positive == 0:
        ten_value_defender_positive = 1
        print(f'Defender success level is: {int(ten_value_defender_positive) // 10}')
    else:
        print(f'Defender success levels is: {success_level_defender}')

    if success_level_attacker > success_level_defender:
        print(f'Attacker wins and gains additional damage of: {int(success_level_attacker) - int(success_level_defender)}. This is addded to strength and weapon damage bonuses. Advantage gained.')
    elif success_level_attacker < success_level_defender:
        print((f'Defender wins and blocks the attack successfully. Advantage gained'))

    again = input("Again? 'y' to continue. Select any other button to quit.")
    if again == "y":
        opposed_roll()
    else:
        print("May the Sigmar guide you")


opposed_roll()
