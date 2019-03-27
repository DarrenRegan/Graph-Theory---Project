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
    self.initial = initial
    self.accept = accept

#Takes single argument which is a postfix regular expression
def compile(postfix):
  nfaStack = []

  for c in postfix:
    accept = state() #create instance of state
    initial = state()
    initial.label = c
    initial.edge1 = accept
    nfaStack.append(nfa(initial, accept)) # Returns instance of nfa setting initial and accept