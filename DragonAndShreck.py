import sys

print("Welcome to dragon Quest")
print("Remember you choices g=have consequences in this game")
print("You have 15 coins in your Pocket spend it wisely")

coins = 15

crossroad = input("crossroad Left / Right ?\n")
if crossroad == "Left":
    print("You died")
    sys.exit(0)
else:
    beggar_choice = input("You have encountered a beggar. He asks you for 7 coins. Yes / No ?\n")
    if beggar_choice == "True":
        coins -= 7

towncenter_choice = input("Your have arrived in towncenter. Right / Middle / Left ? \n")
if towncenter_choice == "Left":
    Shreck = input("you have discovered shreks swamp he can help you for 15 coins. Yes / No \n")
    if coins == 15 and Shreck == "Yes":
        print("Shreck helped you outta swamp. You have survived.")
        sys.exit(0)
    else:
        print("you died because you aer broke")
        sys.exit(0)
elif towncenter_choice == "Middle":
    print('You have arrived in Lion Den you must fight them')
    print('oh no you are injured you will die pretty soon')
    if beggar_choice == "Yes":
        print('The beggar helps you in the fight')
        print('You ve won you have survived')
        sys.exit(0)
    else:
        print('You have died alone')
        sys.exit(0)
else:
    print("You have found the Castle and the Princess.")
    print("now you ll fight the dragon")
    if beggar_choice == "Yes":
        print("Beggar helped you in Dragon fight you have survived")
        sys.exit(0)
    else:
        print("The fight was too hard you have died alone")
        sys.exit(0)
