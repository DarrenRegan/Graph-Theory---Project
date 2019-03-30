# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

# Match Reg Expressions
# Combine Shunt.py and Thompsons.py to create an NFA from a regular expression

# Imports
from shunt import shunt
from thompsons import compile 

def followes(state):
  """Return the set of states that can be reached from state follwoing e arrows"""
  
  # Create a new set, with state as its only member
  states = set()
  states.add(state)
  
  # Check if state has arrows labelled e from it
  if state.label is None:
    if state.edge1 is not None: # Check if edge1 is a state
      states |= followes(state.edge1) # If edge1 exists follow it
    if state.edge2 is not None: # Check if edge2 is a state
      states |= followes(state.edge2) # If edge2 exists follow it

  # Return set of states
  return states

def match(infix, string):
  """Matches string to infix regular expression"""
  
  # Shunt and compile the Reg Ex
  postfix = shunt(infix)
  nfa = compile(postfix)

  # The Current set of states and the next set of states
  current = set() # First empty set
  nextState = set()

  # Add the initial state to current set
  current |= followes(nfa.initial)

  # Loop through each char in string
  for s in string:
    for c in current: # Loop through the current set of states
      # Check if state is labelled s
      if c.label == s:
        nextState |= followes(c.edge1) # Add edge1 state to next set
    # Set current to next, and clear out next
    current = nextState
    nextState = set()

  # Check if the accept state is in the set of current states
  return (nfa.accept in current)

# Tests
infixes = ["a.b?","a.b.c?", "a.(b|d).c+", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["ab", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes: 
  for s in strings:
    print(match(i, s), i, s)