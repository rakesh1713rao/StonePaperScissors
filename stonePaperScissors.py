import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



def function():
    game_images = [rock,paper,scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
    computer_choice = random.randint(0,2)

    if user_choice >= 3 or user_choice < 0:
        print ("Enter the valid number")
    else:
        print(game_images[user_choice])
        print(f"Computer chooses:")
        print(game_images[computer_choice])


    if computer_choice == user_choice:
        print("Match is Draw, Start again.")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
       print("You Win")
    elif user_choice == 2 and computer_choice == 0:
      print("You lose")
    elif user_choice < computer_choice:
     print("You Lose")
    else:
        print("You Win!")

function()