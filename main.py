import random
import time
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



game_images=[rock,paper,scissors]
choice=int(input("How many round you want to play?"))
time.sleep(1.0)
i=0
while i!=choice:
    i+=1
    user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?"))
    time.sleep(0.1)
    if user_choice>=3 or user_choice<0:
        print("Invalid number! You loose.")
    else:
                  print(game_images[user_choice])
                  computer_choice=random.randint(0,2)
                  print("Computer choose")
                  time.sleep(0.1)
                  print(game_images[computer_choice])
                  if user_choice==0 and computer_choice==2:
                      time.sleep(0.1)
                      print("You win!! Congrats.")
                  elif computer_choice==0 and user_choice==2:
                      time.sleep(0.1)
                      print("You loose")
                  elif computer_choice>user_choice:
                      time.sleep(0.1)
                      print("You loose")
                  elif computer_choice<user_choice:
                      time.sleep(0.1)
                      print("You loose")
                  elif user_choice==computer_choice:
                      time.sleep(0.1)
                      print("Draw")
                  else:
                      time.sleep(0.1)
                      print("invalid")
