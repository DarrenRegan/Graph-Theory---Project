# Darren Regan - G00326934 - Software Development Group C
# Graph Theory Project

#Shunting Yard Algorithm
#Takes single argument which is a infix regular expression
def sYard(infix):

  #Order of Precedence: * First > Apply . after * but before | > Apply | last > Treat bracketed groups as individual characters
  specials = {'*': 50, '.': 40, '|': 30} #Dictionary

  postfix = ""
  stack = ""

  for c in infix: #
    if c == '(':
      stack = stack + c #Push ( to the stack
    elif c == ')':
      while stack[-1] != '(': #-1 = last char in string stack
        #Keep finding and poping off the stack until you find the open bracket
        postfix = postfix + stack[-1]
        stack = stack[:-1] #Deleting things from top of stack, Up to but not including last bracket
      stack = stack[:-1] #Removes open bracket
    elif c in specials: #Is c in special Dictionary
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0): #If not there give 0
        #While c Precedence is less then or equal to the Precedence of the last operator on the stack
        postfix = postfix + stack[-1]
        stack = stack[:-1]
      stack = stack + c
    else:
      postfix = postfix + c

  while stack:
    #Take end of stack put it onto postfix, then remove it from the stack
    postfix = postfix + stack[-1]
    stack = stack[:-1]

  return postfix

print(sYard("(a.b)|(c*.d)"))