from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FILE = "high_score.txt"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.load_high_score()
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.hideturtle()
    self.update_scoreboard()
  
  def load_high_score(self):
    """Load high score from file, return 0 if file doesn't exist"""
    try:
      with open(HIGH_SCORE_FILE, "r") as file:
        return int(file.read())
    except:
      return 0
  
  def save_high_score(self):
    """Save high score to file"""
    with open(HIGH_SCORE_FILE, "w") as file:
      file.write(str(self.high_score))
    
  def update_scoreboard(self):
    self.clear()
    self.goto(0, 270)
    self.color("white")
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    # Display high score in gold color
    self.goto(0, 240)
    self.color("#ffd700")  # Gold color for high score
    self.write(f"Highest Score: {self.high_score}", align=ALIGNMENT, font=("Courier", 18, "normal"))
  
  def increase_score(self):
    self.score += 1
    self.update_scoreboard()
    
  def game_over(self):
    # Check if new high score
    if self.score > self.high_score:
      self.high_score = self.score
      self.save_high_score()
      self.goto(0, 30)
      self.color("#ffd700")
      self.write("NEW HIGHEST SCORE! 🎉", align=ALIGNMENT, font=("Courier", 20, "bold"))
    
    self.goto(0, 0)
    self.color("#ff6b6b")  # Red color for game over
    self.write("GAME OVER!", align=ALIGNMENT, font=("Courier", 28, "bold"))