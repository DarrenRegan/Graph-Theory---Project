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

  # Constructor, self = current instance of class
  def __init__(self, initial, accept):
    self.initial = initial
    self.accept = accept

# Takes single argument which is a postfix regular expression
def compile(postfix):
  nfaStack = []

  for c in postfix:
    if c == '.':
      # Pop two NFA's off stack
      nfa2 = nfaStack.pop()# Take last element of array out of array and return it
      nfa1 = nfaStack.pop()
      nfa1.accept.edge1 = nfa2.initial # Take edge 1 and set to intial state of nfa2
      nfaStack.append(nfa(nfa1.initial, nfa2.accept))
    elif c == '|':
      # Pop two NFA's off the stack
      nfa2 = nfaStack.pop()
      nfa1 = nfaStack.pop()
      # Create new initial state, connect it to initial states of the two NFA's popped from the stack
      initial = state()
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial
      # Create a new accept state, connect the accept states of the two NFA's popped from the stack, to the new state
      accept = state()
      nfa1.accept.edge1 = accept #points to new accept state
      nfa2.accept.edge1 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    elif c == '*':
      # Pop single NFA from the stack
      nfa1 = nfaStack.pop()
      # Create new initial and accept states
      initial = state()
      accept = state()
      # Join the new initial state to nfa1's intial state and the new accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept
      # Join the old accept state to the new accept state and nfa1's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    elif c == '+':
      # Pop single NFA from the stack
      nfa1 = nfaStack.pop()
      # Create new initial and accept states
      initial = state()
      accept = state()
      # Joining states
      nfa2 = nfa(initial, accept)
      nfa1.accept.edge1 = nfa1.initial 
      nfa1.accept.edge2 = nfa2.initial
    


    elif c == '?':
      # Pop single NFA from the stack
      nfa1 = nfaStack.pop()
      # Create new initial and accept states
      initial = state()
    else:
      accept = state() # Create instance of state
      initial = state()
      initial.label = c
      initial.edge1 = accept
      nfaStack.append(nfa(initial, accept)) # Returns instance of nfa setting initial and accept

  # nfaStack should only have a single nfa on it at this point
  return nfaStack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))