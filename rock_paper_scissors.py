import random

class RockPaperScissors:
  def __init__(self):
    self.player_name = ''
    self.rounds = 3
    self.choices = { '1': 'rock', '2': 'paper', '3': 'scissors' }
    self.computer_choice = ''
    self.player_choice = ''
    self.num_of_wins = 0
  
  def start(self):
    self.intro()
    i = 1
    while i <= self.rounds:
      print(f"\n=== ROUND {i} ===")
      self.player_choice = self.user_pick()
      self.computer_choice = "".join(random.sample(list(self.choices.values()), 1))
      
      if not self.player_choice.isdigit() or int(self.player_choice) not in range(1,4):
        print(f"\n {self.player_choice} is not a valid option. Please try again.\n")
        continue
      else:
        self.determine_game_result(i)

      i +=  1
  
  def intro(self):
    self.player_name = input("Enter your name: ")
    print(f"Hi, {self.player_name}! Let's get started...")
  
  def user_pick(self):
    for idx, element in enumerate(self.choices):
      print(f"{idx + 1}. {self.choices[element]}")
    return input("Please choose a number: ")
  
  def is_winner(self):
    p = self.choices[self.player_choice]
    c = self.computer_choice

    if (p == "rock" and c == "scissors") or (p == "scissors" and c == "paper") or (p == "paper" and c == "rock"):
      return True
    else:
      return False
  
  def determine_game_result(self, round):
    if round == 3:
      if self.num_of_wins >= 2:
        print(f"\nCongratulations, {self.player_name} won the game!")
      else:
        print(f"\nAw, {self.player_name} lost this game :(")
    elif self.is_winner():
      print("You won this round!")
      self.num_of_wins += 1
    else:
      print("You lost this round.")

