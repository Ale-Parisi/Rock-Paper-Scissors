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

import random
pc = random.randint(0,2)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)

print("Computer chose:")

if pc == 0:
  print(rock)
elif pc == 1:
  print(paper)
elif pc == 2:
  print(scissors)

if player == 0 and pc == 2 or player == 1 and pc == 0 or player == 2 and pc == 1:
  print("You Win!")
elif player == 0 and pc == 1 or player == 1 and pc == 2 or player == 2 and pc == 0:
  print("You Lose!")
elif player == 0 and pc == 0 or player == 1 and pc == 1 or player == 2 and pc == 2:
  print("Draw.")