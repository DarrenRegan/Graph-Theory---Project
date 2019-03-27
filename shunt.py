# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

#Takes single argument which is a infix regular expression
def sYard(infix):

  #Order of Precedence: * First > Apply . after * but before | > Apply | last > Treat bracketed groups as individual characters
  specials = {'*': 50, '.': 40, '|': 30} #Dictionary

  postfix = ""
  stack = ""


  for c in infix: #
    if c == '(':

    elif c == ')':

    elif c in specials: #Is c in special Dictionary

  return postfix