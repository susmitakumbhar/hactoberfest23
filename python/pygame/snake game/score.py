FONT1 = ('courier', 14, 'normal')
FONT = ('courier', 18, 'bold')
import turtle as t
class Score(t.Turtle):
   def __init__(self):
      super().__init__()
      self.scores = 0
      self.ht()
      self.penup()
      self.goto(-280,280)
      self.color("white")
      self.printScore()
   def update(self):
      self.scores += 1
      self.clear()
   def gameOver(self):
      self.goto(0, 0)
      self.write("Game Over", align = "left", font=FONT)
   def printScore(self):
      
      self.write(f"YOUR SCORE: {self.scores}", align = "left", font=FONT1)