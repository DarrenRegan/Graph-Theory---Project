# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

# Combine Shunt.py and Thompsons.py to create an NFA from a regular expression

def match(infix, string):
  """Matches string to infix regular expression"""
  # Shunt and compile the Reg Ex
  postfix = shunt(infix)
  nfa = compile(postfix)

  # The Current set of states and the next set of states
  current = set()
  nexts = set()

  # Loop through each char in string
  for s in string: