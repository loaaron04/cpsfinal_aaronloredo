import random

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    restart = input("Do you want to roll the dices again?(y/n)")
    if restart == "y" or restart == "Y":
        game()


if __name__ == "__main__":
    game()
