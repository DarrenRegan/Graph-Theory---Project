# Graph-Theory---Project
G00326934 - Graph Theory Project - build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

# Run program
```
1. Clone Git Repo OR Download Zipped folder from github and unzip the folder
2. Open unzipped folder/Cloned Git Repo and type cmd in file explorer to open the folder in command promt
3. Once in the folder in command line type python matchRegEx.py to execute script
```

## Examples of Regular Expressions
1. a.b.c   - a single (a) followed by a single (b) followed by a single (c)
2. a.b.c*  - an (a) followed by a (b) followed by zero or more (c's)
3. a|b.c   - an (a), or a (b) followed by a (c)
4. (a|b).c - an (a) or a (b), followed by a (c)
5. 0.0.(0|1)* - all strings of 0's and 1' that begin with two zeros
6. 1* - any number of 1's (including empty string)

## Precedence
1. Always apply * first
2. Apply . after * but before |
3. Apply | last
4. Treat bracketed groups as individual characters

## Infix & Postfix
1. Much rather use postfix notation then infix because it will make algorithms simpler
2. Convert infix notation to postfix with The Shunting Yard Algorithm

## Thompson's Construction
1. Algorithm constructs NFA's from a regular expression i.e(a.b|b*)
2. Thompson's end up with alot of (e) arrows
3. Works on Fragments of NFA's, fragment is a smaller NFA
4. Take these smaller NFA's, stack up like lego blocks to build a bigger NFA

## Shunting Yard Algorithm
1. Converts an infix expression into a postfix expression
2. It uses a stack
3. The purpose of the stack is to reverse the order of the operators in the expression

## Quick Note on + & ? Operators in Thompsons

    ```
    elif c == '+':
      1. Pop a single NFA from the stack
      2. Create new initial and accept states
      3. Join the state(s)
      4. Join the old accept state to the new accept state and nfa1's initial state
      5. Push new NFA to the stack with .append(nfa(initial, accept))
    ```

    ```
    elif c == '?':
      1. Pop a single NFA from the stack
      2. Create new initial and accept states
      3. Join the state(s)
      4. Join the old accept state to the new accept state and nfa1's initial state
      5. Push new NFA to the stack with .append(nfa(intiial, accept))
    ```


# References

* [Video](https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e) - Shunting Yard Algorithm by Hand
* [Video](https://web.microsoftstream.com/video/29de6c7c-9379-46d3-99e8-8a3dbafe391f) - Thompson's Construction by Hand

* [Shunt Yard](http://www.oxfordmathcenter.com/drupal7/node/628) - Excellent resouce explaining the Shunting Yard Algorithm
* [regexp](https://swtch.com/~rsc/regexp/regexp1.html) - Resource explaining two approaches to Regular Expressions including the performance differences
* [Book by Jake VanderPlas](https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf)
* [Infix-Pofix](https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix) - Resource explaining infix-postfix with code examples in 5 different languages (C++, C, Java, Python, C#)
* [Python](http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html) - Resource for Infix, Prefix and Postfix Expressions

# Author
* [Darren Regan](https://github.com/DarrenRegan)

