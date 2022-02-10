print(
	'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
      Welcome to TREASURE ISLAND! Your mission is to find the treasure.                           
*******************************************************************************'''
)

while True:
    user_input = input('\nYou found yourself on an island. You can go "left" or "right". Where would you go? ').casefold()
    while user_input not in ['left', 'right']:
        user_input = input('Invalid input. Please enter "left" or "right". ').casefold()
    if user_input == 'right':
        print('\nYou fell into a hole and died. GAME OVER.')
        break
    elif user_input == 'left':
        user_input = input('\nYou came to the river. What do you want to do, "swim" across or "wait" for the boat? ').casefold()
        while user_input not in ['swim', 'wait']:
            user_input = input('Invalid input. Please enter "swim" or "wait". ').casefold()
        if user_input == 'swim':
            print('\nYou been eaten by an aligator. GAME OVER.')
            break
        elif user_input == 'wait':
            user_input = input('\nYou came across the river and entered a room.'
                               '\nThere are three doors in front of you: "red", "yellow" and "blue". Which room will you enter? ').casefold()
            while user_input not in ['red', 'yellow', 'blue']:
                user_input = input('Invalid input. Please enter "red", "yellow", or "blue". ').casefold()
            if user_input == 'red':
                print("\nYou've entered a room or fire and you were burned to death. GAME OVER.")
                break
            elif user_input == 'blue':
                print("\nYou've entered a room full of rats and you were eaten. GAME OVER.")
                break
            elif user_input == 'yellow':
                print("\nYou've found the treasure! YOU WIN!")
                break
