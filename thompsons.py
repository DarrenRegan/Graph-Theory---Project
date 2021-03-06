# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

#Thompsons Algorithm
#Creating NFA's

class state:
  label, edge1, edge2 = None, None, None


class nfa:
  initial, accept = None, None

  # Constructor, self = current instance of class
  def __init__(self, initial, accept):
    self.initial = initial
    self.accept = accept 

# Takes single arugment which is a postfix regular expression
def compile(profix):
  nfaStack = []

  for c in profix:
    if c == '.':
      # pop two NFA's off the stack
      # Take last element of array out of array and return it
      nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
      nfa1.accept.edge1 = nfa2.initial
      nfaStack.append(nfa(nfa1.initial, nfa2.accept))
    elif c == '|':
      # Pop two NFA's off the stack
      nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
      # Create new initial state, connect it to initial states of the two NFA's popped from the stack
      initial, accept  = state(), state()
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial
      # Create a new accept state, connect the accept states of the two NFA's popped from the stack, to the new state
      nfa1.accept.edge1 = accept
      nfa2.accept.edge1 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    elif c == '*':
      # Pop a single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creat new initial and accept states
      initial, accept  = state(), state()
      # Join the new initial state to nfa1's initial state and the new accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept
      # Join the old accept state to the new accept state and nfa1's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    elif c == '+':
      # Pop a single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creat new initial and accept states
      initial, accept  = state(), state()
      # Joining States
      initial.edge1 = nfa1.initial
      # Join the old accept state to the new accept state and nfa1's initial state
      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    elif c == '?':
      # Pop a single NFA from the stack
      nfa1 = nfaStack.pop()
      # Creat new initial and accept states
      initial, accept  = state(), state()
      # Joining States
      initial.edge1 = nfa1.initial
      initial.edge2 = accept
      # Join the old accept state to the new accept state and nfa1's initial state
      nfa1.accept.edge1 = accept
      # Push new NFA to the stack
      nfaStack.append(nfa(initial, accept))
    else: 
      initial, accept  = state(), state() # Create instances of state
      initial.label = c
      initial.edge1 = accept
      nfaStack.append(nfa(initial, accept)) # Returns instance of nfa setting initial and accept

  # nfaStack should only have a single nfa on it at this point
  return nfaStack.pop()
  
#print(compile("ab.cd.|"))
#print(compile("aa.*"))
#print(compile("aa.+"))
#print(compile("aa.?"))