
<<<<<<< HEAD
<<<<<<< HEAD
# Quick Notes
=======
# Notes
>>>>>>> 01160648a9446e3d0f0671e71f86f958defd9de5
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
1. 
2. 
3. 
4. 


# References

Shunting Yard Algorithm by Hand
https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e

http://www.oxfordmathcenter.com/drupal7/node/628     
https://swtch.com/~rsc/regexp/regexp1.html    
https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
<<<<<<< HEAD

=======
https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
>>>>>>> 01160648a9446e3d0f0671e71f86f958defd9de5
http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
=======
>>>>>>> 8becf371a17e8527c4a8039c60aa2456a048b2ee
