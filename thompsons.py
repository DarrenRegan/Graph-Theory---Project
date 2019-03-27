# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

#Thompsons Algorithm
#Creating NFA's

class state:
  lable = None
  edge1 = None
  edge2 = None

class nfa:
  initial = None
  accept = None

  #Constructor, self = current instance of class
  def __init__(self, initial, accept):