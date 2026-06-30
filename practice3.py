#Rock,Paper,Scissor with computer
import random
options=["Rock","Paper","Scissor"]
player=None
player_wins=0
computer_wins=0
tie=0
while True:
    computer = random.choice(options)
    player=input("\nEnter (Rock, Paper, Scissor)?(q to quit):\n==> ").strip().title()
    print(f"\nComputer = {computer}")
    if player.lower() == "q":
        break
    if  player not in options:
        print("\nInvalid input. Please try again.\n")
        continue
    elif player==computer:
       print("It's a tie!")
       tie+=1
    elif ((player=="Rock" and computer=="Scissor") or
        (player=="Paper" and computer=="Rock")or
         (player =="Scissor" and computer=="Paper")
    ):
        print("You won!")
        player_wins+=1
    else:
        print("\nComputer won!.")
        computer_wins+=1
print("\nResults:")
print(f"Computer won = {computer_wins} time.")
print(f"Player won = {player_wins} time.")
print(f"Tie = {tie} times.")

