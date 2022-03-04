This was a school project where we were needed to create a Lexical Analyzer, a Parser, and an Interpreter
that could take in a .jl file with a special type of syntax and be able to fully execute the code within.

The Lexical Analyzer takes in the file and splits the words within into tokens. The Parser groups those 
tokens together based on their ordering. The Interpreter executes the parsed statements.

This specialized syntax was fairly simple in that variable names were only 1 letter long and we did not 
need to implement every function that would normally be present in an IDE. Additionally only integers were
allowed to be used for math functions and assignments.

The name of the file that needs to be read must be manually changed on line 34 if different files are to be read.

What functions are implemented:
Many math functions (addition, subtraction, multiplication, division, modulo)

Variable support (variable store values and are executed as the number stored within them)

Many math equals function ("+=", "-=", "*=", "/=")

Parenthesis support (5 * (2 + 2) will equal 20 and not 12)

Boolean operator support (">", "<", ">=", "<=", "==", "~=")

If Statement support 

If Then Statement support

While Statement support

Do While Statement support

Print Statement support

Function support
