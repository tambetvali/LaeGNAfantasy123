
# How much, comparatively, would have been multiplied, if this is added.
def velocityCompensation(total, next):


class CalculatorExpression:
  def __init__(self, number = 0.0):
    self.start(number)

  # We dont need each part of this log - we need Tnum, Radd and Rmul.
  # However, let's watch more variables.
  def start(self, number = 0.0):
    # 0 is neutral towards addition, and we measure it this way
    self.Radd = 0.0
    self.Tadd = 0.0

    # Rather 1 is neutal towards absolute value in multiplication
    self.Rmul = 1.0
    self.Tmul = 1.0

  def add(self, number):
    self.addCor()
    self.Tadd += number
  
  def mul(self, number):
    self.register(self.Tadd, self.Tadd + number)
    self.Tmul *= number
  
