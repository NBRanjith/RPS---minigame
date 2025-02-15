import random

my_game = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor:"))

if my_game == 0:
    print("My choice:" + "Rock")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif my_game == 1:
    print("My choice:" + "Paper")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif my_game == 2:
    print("My choice:" + "Scissors")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


computer_game = random.randint(0,2)
print(f"Computer Choice is :{computer_game}")

if computer_game == 0:
    print("Computer choice:" + "Rock")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_game == 1:
    print("Computer choice:" + "Paper")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

else:
    print("Computer choice:" + "Scissors")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
if my_game >=3 or my_game < 0:
    print("you typed an invalid number. You Lose!")
elif my_game == 0 and computer_game == 2:
    print("You win!")
elif computer_game > my_game:
    print("You Lose!")
elif computer_game == 0 and my_game == 2:
    print("You Lose!")
elif my_game > computer_game:
    print("You Win!")
elif computer_game == my_game:
    print("It is a Draw!")
