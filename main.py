#
# * Class:       CS 4308 Section 02
# * Term:        Fall 2021
# * Name:       <Paul Neamtu>
# * Instructor:   Sharon Perry
# * Project:     Deliverable 2 Parser
#

#import some useful directories
import re
import string

####################################
"-----------SCANNER-----------------"
####################################

#token class to store the values of each token created by the SCANNER
class Token:
    def __init__(self, name, value, place):
        self.name = name
        self.value = value
        self.place = place

    def __repr__(self):
        if self.value: return f'{self.name}:{self.value}'
        return f'{self.type}'

#function to remove // comments from the original file
def removeComments(str):
    str = re.sub(re.compile("//.*?\n" ) ,"" ,str)
    return str

#open the test file and convert it to a string and remove // comments
file = open("Test1.jl")
lines = file.read()
lines = removeComments(lines)

#split the string into a list based on all the expected places to split
lines = re.split('( )|\n|\t|([(])|([)])|(>)|(<)|([+])|(-)|([*])|(/)|(=)',lines)

#remove None and blank spaces from the list
blank = ''
No_None = filter(None.__ne__, lines)
lines = list(No_None)
No_Blanks = filter(lambda x: x != "", lines)
lines = list(No_Blanks)

#list of all operators and all operator names
operators = ["=", "+", "-", "/", "*", "(", ")", ">", "<", ">=", "<=", "==", "~=", "+=", "-=", "*=", "/=", "~"]
operatorNames = ["Assignment_Operator", "Addition_Operator", "Subtraction_Operator", "Division_Operator",
                 "Multiplication_Operator", "Open_Parentheses", "Closed_Parentheses", "GT_Operator",
                 "LT_Operator", "GE_Operator", "LE_Operator", "EQ_Operator", "NE_Operator", "PE_Operator",
                 "ME_Operator", "MultEq_Operator", "DivEq_Operator", "NOT_Operator"]

#list of all identifiers since our simplified version of Julia only takes single letters as identifiers
identifiers = string.ascii_lowercase
identifiersAlso = string.ascii_uppercase

#list of all keywords and all keyword names
keyWords = ["function", "print", "end", "if", "else", "then", "while", "do"]
keyWordNames = ["FUNCTION", "PRINT", "end", "IF_Statement", "ELSE_Statement",
                "THEN_Statement", "WHILE_Statement", "DO_Statement"]

i = 0
over = 0
count = 0
tokens = []
#loop through the list until everything is either tokenized or there is an error
while(i < len(lines)):
    #if loop too many times throw an error because something is wrong
    if(over > len(lines)):
        i = len(lines)
        print("error with file!")

    #skip over spaces
    if(lines[i] == " "):
        i += 1

    if (lines[i] != " "):
        # determine if an integer is present
        if (lines[i].isnumeric()):
            #print("Lexeme: " + lines[i] + "                                   Token: INTEGER")
            tokens.append(Token("INTEGER", lines[i], count))
            count += 1
            i += 1

        # loop through the operator table to determine if the current lexeme is an operator
        for j in range(len(operators)):
            if (i < len(lines) and lines[i] == operators[j]):
                #parenthases do not need any special conditions since nothing can come after them to make a new operator
                if (operators[j] == "(" or operators[j] == ")"):
                    #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                    tokens.append(Token(operatorNames[j], operators[j], count))
                    count += 1
                    i += 1
                    break

                if(operators[j] != "(" or operators[j] != ")"):
                    #every operator below here changes whether there is an = or not so each one needs to be checked for =
                    if(operators[j] == "+" and lines[i+1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i+1] + "                                   Token: " + operatorNames[13])
                        tokens.append(Token(operatorNames[13], operators[13], count))
                        count += 1
                        i += 2
                        break
                    elif(operators[j] == "+" and lines[i+1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (lines[i] == "-" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[14])
                        tokens.append(Token(operatorNames[14], operators[14], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "-" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == "*" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[15])
                        tokens.append(Token(operatorNames[15], operators[15], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "*" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == "/" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[16])
                        tokens.append(Token(operatorNames[16], operators[16], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "/" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == ">" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[9])
                        tokens.append(Token(operatorNames[9], operators[9], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == ">" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == "<" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[10])
                        tokens.append(Token(operatorNames[10], operators[10], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "<" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == "=" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[11])
                        tokens.append(Token(operatorNames[11], operators[11], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "=" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

                    if (operators[j] == "~" and lines[i + 1] == "="):
                        #print("Lexeme: " + operators[j] + lines[i + 1] + "                                   Token: " + operatorNames[12])
                        tokens.append(Token(operatorNames[12], operators[12], count))
                        count += 1
                        i += 2
                        break
                    elif (operators[j] == "~" and lines[i + 1] != "="):
                        #print("Lexeme: " + operators[j] + "                                   Token: " + operatorNames[j])
                        tokens.append(Token(operatorNames[j], operators[j], count))
                        count += 1
                        i += 1
                        break

        #loop through possible identifiers and mark it as such if it is
        for j in range(len(identifiers)):
            if (i < len(lines) and lines[i] == identifiers[j] or i < len(lines) and lines[i] == identifiersAlso[j]):
                #print("Lexeme: " + lines[i] + "                                   Token: Identifier")
                tokens.append(Token("Identifier", lines[i], count))
                count += 1
                i += 1
                break

        #loop through the list of keywords to check if current lexeme is keyword
        for j in range(len(keyWords)):
            if (i < len(lines) and lines[i] == keyWords[j]):
                #print("Lexeme: " + lines[i] + "                                   Token: " + keyWordNames[j])
                tokens.append(Token(keyWordNames[j], lines[i], count))
                count += 1
                i += 1
                break
    #add after each while loop so that the error will work
    over += 1

#for i in tokens:
#    print(i.__repr__())



####################################
"-----------PARSER-----------------"
####################################

#node for integers
class IntNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'

#node for end keyword
class endNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'

#node for variables
class VarNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'

#node for math operator functions
#takes in a left hand side, an operator, and a right hand side
class mathOpNode:
    def __init__(self, leftNode, op, rightNode, place):
        self.leftNode = leftNode
        self.op = op
        self.rightNode = rightNode
        self.place = place

    def __repr__(self):
        return f'({self.leftNode}, {self.op}, {self.rightNode})'

#node for boolean operator functions
#takes in a left hand side, an operator, and a right hand side
class boolOpNode:
    def __init__(self, leftNode, boolOp, rightNode):
        self.leftNode = leftNode
        self.boolOp = boolOp
        self.rightNode = rightNode

    def __repr__(self):
        return f'({self.leftNode}, {self.boolOp}, {self.rightNode})'

#node for an assignment operator function
#takes in a left hand side, an equals sign(whether that be =, +=, -=, etc.), and a right hand side
class assignOpNode:
    def __init__(self, leftNode, EQ, rightNode):
        self.leftNode = leftNode
        self.EQ = EQ
        self.rightNode = rightNode

    def __repr__(self):
        return f'({self.leftNode}, {self.EQ}, {self.rightNode})'

#node for if statement functions
#takes in an if variable, an expression, a then variable, another expression, and ends with the end keyword
class IfStatementNode:
    def __init__(self, ifVar, exprOne, thenVar, exprTwo, endVar):
        self.ifVar = ifVar
        self.exprOne = exprOne
        self.thenVar = thenVar
        self.exprTwo = exprTwo
        self.endVar = endVar

    def __repr__(self):
        return f'({self.ifVar}, {self.exprOne}, {self.thenVar}, {self.exprTwo}, {self.endVar})'

#node for if else functions
#exactly like if statements but has an extra else variable and a third expression for it
class IfElseStatementNode:
    def __init__(self, ifVar, exprOne, thenVar, exprTwo, elseVar, exprThree, endVar):
        self.ifVar = ifVar
        self.exprOne = exprOne
        self.thenVar = thenVar
        self.exprTwo = exprTwo
        self.elseVar = elseVar
        self.exprThree = exprThree
        self.endVar = endVar

    def __repr__(self):
        return f'({self.ifVar}, {self.exprOne}, {self.thenVar}, {self.exprTwo}, {self.elseVar}, {self.exprThree}, {self.endVar})'

#node for while statement functions
#takes in a while variable, a boolean expression, a do variable, and then blocks in every expression until an end variable is reached
class WhileStatementNode:
    def __init__(self, whileVar, boolExpr, doVar, doStuff, endVar):
        self.whileVar = whileVar
        self.boolExpr = boolExpr
        self.doVar = doVar
        self.doStuff = doStuff
        self.endVar = endVar

    def __repr__(self):
        return f'({self.whileVar}, {self.boolExpr}, {self.doVar}, {self.doStuff}, {self.endVar})'

#node for print statement functions
#takes in a print variable, an open parentheses, the expression to be printed, and an end parentheses
class PrintStatementNode:
    def __init__(self, printVar, parOne, printExpr, parTwo):
        self.printVar = printVar
        self.parOne = parOne
        self.printExpr = printExpr
        self.parTwo = parTwo

    def __repr__(self):
        return f'({self.printVar}, {self.parOne}, {self.printExpr}, {self.parTwo})'

#node for functions
#takes in the function variable, the function id, the open and closed parentheses, then blocks in everything until an end variable is reached
class FunctionNode:
    def __init__(self, funcVar, funcId, parOne, parTwo, everything, endVar):
        self.funcVar = funcVar
        self.funcId = funcId
        self.parOne = parOne
        self.parTwo = parTwo
        self.everything = everything
        self.endVar = endVar

    def __repr__(self):
        return f'({self.funcVar}, {self.funcId}, {self.parOne}, {self.parTwo}, {self.everything}, {self.endVar})'

#Parser class
#This takes in the token list we generated in the lexical analyzer
class Parser:
    #constructor
    def __init__(self, Alltokens):
        self.Alltokens = Alltokens
        self.tokIdx = -1
        self.advance()

    #advance function to move the token index
    #we use this to chunk through the token list while we block everything into place
    def advance(self):
        self.tokIdx += 1
        if self.tokIdx < len(self.Alltokens):
            self.currTok = self.Alltokens[self.tokIdx]
        return self.currTok

    #this method starts the parsing
    def parse(self):
        res = self.expr()
        return res

    #this is the lowest state for our Parser
    #this is where we get to our identifiers, and our integers
    def factor(self):
        token = self.currTok

        if token.name == "Identifier":
            self.advance()
            return VarNode(token)

        if token.name == "INTEGER":
            self.advance()
            return IntNode(token)

    #this is our term method where we handle multiplication and division
    #we have a different method for this because multiplication and division must happen before addition and subtraction
    def term(self):
        left = self.factor()

        while self.currTok.value == operators[3] or self.currTok.value == operators[4]:
            oper = self.currTok
            self.advance()
            right = self.factor()
            left = mathOpNode(left, oper, right, self.tokIdx)

        return left

    #this is our starter expression method
    #this is where we handle most of our keyword functions such as print, if, while_do, etc...
    def expr(self):

        #this part of the expression function handles what happens to our identifiers
        if self.currTok.name == "Identifier":
            varName = self.currTok
            self.advance()
            if self.currTok.value != operators[0]:
                #if a boolean operator comes after our identifier we block it into a boolean operator node
                if self.currTok.value == operators[7] or self.currTok.value == operators[8] or self.currTok.value == operators[9] or self.currTok.value == operators[10] or self.currTok.value == operators[11] or self.currTok.value == operators[12]:
                    boolOp = self.currTok
                    self.advance()
                    expr = self.expr()
                    return boolOpNode(varName, boolOp, expr)

                #if a plus or minus comes after our identifier we have to block it in a math operator node
                #we also need to call our term method just in case some multiplication or division shenanigans happen
                if self.currTok.value == operators[1] or self.currTok.value == operators[2]:
                    var = self.term()
                    while self.currTok.value == operators[1] or self.currTok.value == operators[2]:
                        mathOp = self.currTok
                        self.advance()
                        right = self.term()
                        var = mathOpNode(varName, mathOp, right, self.tokIdx)
                    return var

                #if a multiplication or division symbol comes after our identifier we also block it into a math operator node
                #for this i pretty much just copied and pasted the code from term to handle the multiplication/division
                #we also do this in a seperate if statement from our + and - because of math precedents
                if self.currTok.value == operators[3] or self.currTok.value == operators[4]:
                    var = self.factor()

                    while self.currTok.value == operators[3] or self.currTok.value == operators[4]:
                        oper = self.currTok
                        self.advance()
                        right = self.factor()
                        var = mathOpNode(varName, oper, right, self.tokIdx)
                    return var

            #lastly if any kind of equals sign comes after our identifier we block it into an assignment operator node
            #if nothing of significance comes after our identifier, we simple return the identifier
            if self.currTok.value == operators[0] or self.currTok.value == operators[13] or self.currTok.value == operators[14] or self.currTok.value == operators[15] or self.currTok.value == operators[16]:
                EQ = self.currTok
                self.advance()
                expr = self.expr()
                return assignOpNode(varName, EQ, expr)
            else:
                return varName


        #this is how we handle if statements
        #if we detect an if statement we check to make sure it has the proper syntax otherwise we print a simple error message
        if self.currTok.name == "IF_Statement":
            ifVar = self.currTok
            self.advance()
            exprOne = self.expr()
            #self.advance()
            if self.currTok.name != "THEN_Statement":
                print("expected 'then' statement")
            elif self.currTok.name == "THEN_Statement":
                thenVar = self.currTok
                self.advance()
                exprTwo = self.expr()

                #if everything is up to code we then check if this is an if statement or an if else statement
                #if it is an if statement we block everything into an if statement node and if not we block it into an if_else statement node
                if self.currTok.name != "ELSE_Statement":
                    if self.currTok.name == "end":
                        endVar = self.currTok
                        final = IfStatementNode(ifVar, exprOne, thenVar, exprTwo, endVar)
                        return final
                    else:
                        return print("expected 'end'")
                elif self.currTok.name == "ELSE_Statement":
                    elseVar = self.currTok
                    self.advance()
                    exprThree = self.expr()
                    if self.currTok.name == "end":
                        endVar = self.currTok
                        final = IfElseStatementNode(ifVar, exprOne, thenVar, exprTwo, elseVar, exprThree, endVar)
                        return final
                    else:
                        return print("expected 'end'")


        # this is how we handle while statements
        # if we detect a while statement we check to make sure it has the proper syntax otherwise we print a simple error message
        if self.currTok.name == "WHILE_Statement":
            whileVar = self.currTok
            self.advance()
            if self.currTok.name == "Identifier":
                varName = self.currTok
                self.advance()
                if self.currTok.value != operators[0]:
                    if self.currTok.value == operators[7] or self.currTok.value == operators[8] or self.currTok.value == operators[9] or self.currTok.value == operators[10] or self.currTok.value == operators[11] or self.currTok.value == operators[12]:
                        boolOp = self.currTok
                        self.advance()
                        expr = self.expr()
                        boolExpr =  boolOpNode(varName, boolOp, expr)
            else:
                return print("expected boolean expression")

            if self.currTok.name != "DO_Statement":
                print("expected 'do' statement")
            elif self.currTok.name == "DO_Statement":
                doVar = self.currTok
                self.advance()
                totalDoStuff = []
                doStuff = self.expr()
                totalDoStuff.append(doStuff)
                #while statements are special because we need to block every expression in them until we reach an end keyword
                while self.currTok.name != "end":
                    doStuff = self.expr()
                    totalDoStuff.append(doStuff)
                endVar = self.currTok
                self.advance()
                #if there are no errors we block the while statement into a while statement node
                final = WhileStatementNode(whileVar, boolExpr, doVar, totalDoStuff, endVar)
                return final

        # this is how we handle print statements
        # if we detect a print statement we check to make sure it has the proper syntax otherwise we print a simple error message
        if self.currTok.name == "PRINT":
            printVar = self.currTok
            self.advance()
            if self.currTok.value != operators[5]:
                return print("Expected (")
            elif self.currTok.value == operators[5]:
                parOne = self.currTok
                self.advance()
                printExpr = self.expr()
                if self.currTok.value != operators[6]:
                    return print("Expected )")
                elif self.currTok.value == operators[6]:
                    parTwo = self.currTok
                    self.advance()
                    #if there are no errors we block it into a print statement node
                    final = PrintStatementNode(printVar, parOne, printExpr, parTwo)
                    return final

        # this is how we handle functions
        # if we detect a function we check to make sure it has the proper syntax otherwise we print a simple error message
        if self.currTok.name == "FUNCTION":
            funcVar = self.currTok
            self.advance()
            if self.currTok.name != "Identifier":
                return print("identifier expected")
            elif self.currTok.name == "Identifier":
                funcId = self.currTok
                self.advance()
                if self.currTok.value != operators[5]:
                    return print("Expected (")
                elif self.currTok.value == operators[5]:
                    parOne = self.currTok
                    self.advance()
                    if self.currTok.value != operators[6]:
                        return print("Expected )")
                    elif self.currTok.value == operators[6]:
                        parTwo = self.currTok
                        self.advance()
                        everything = []
                        #like while loops functions need to take in every single expression that occurs until an end keyword is reached
                        while self.currTok.name != "end":
                            current = self.expr()
                            everything.append(current)
                        endVar = self.currTok
                        #if there are no errors we block the whole function into a function node
                        final = FunctionNode(funcVar, funcId, parOne, parTwo, everything, endVar)
                        return final


        ##this is how we handle end keywords
        #end keywords are special because it stops the current expression
        if self.currTok.name == "end":
            self.advance()
            return endNode(self.currTok)


        #finally this is how we handle regular non-variable math
        left = self.term()
        #after assigning our left hand side we loop through the term function until everything fits within the precedence of PEMDAS
        while self.currTok.value == operators[1] or self.currTok.value == operators[2]:
            oper = self.currTok
            self.advance()
            right = self.term()
            left = mathOpNode(left, oper, right, self.tokIdx)

        #this is how we handle number boolean operations
        #while number on number boolean expressions are not common we should still catch them
        while self.currTok.value == operators[7] or self.currTok.value == operators[8] or self.currTok.value == operators[9] or self.currTok.value == operators[10] or self.currTok.value == operators[11] or self.currTok.value == operators[12]:
            oper = self.currTok
            self.advance()
            right = self.term()
            left = boolOpNode(left, oper, right)

        return left


####################################
"-----------Interpreter-----------------"
####################################
#this is the Interpreter class where we use all the information we gathered from the parse and scanner classes to actually execute the code

#this is a class that holds all the variables we have for the code
#it makes it so if "x = 4" is written on one line it will be evaluated as 4 in a later line
class VariableHolder:
    #Variable Holder is initialized as a list
    def __init__(self):
        self.vars = []

    #function that grabs the variable from the list
    def get(self, name):
        for i in self.vars:
            if (i.name == name):
                return i.value

    #this function appends a variable to the list
    #since the variable needs both a name and a value I just reused the token object I created for the tokens since that object holds a name and value
    def set(self, name, value):
        count = 0
        for i in self.vars:
            if(i.name == name):
                self.vars[count] = Token(name, value, 0)
                count = -1
                break
            count += 1

        identifier = Token(name, value, 0)
        self.vars.append(identifier)

#this class acts as a holder for values and makes it so we can perform operations a=on them
class Number:
    def __init__(self, val):
        self.val = val

    #all these are simple math operations that we have to operate on the Number objects we create
    def add(self, right):
        return Number(self.val + right.val)
    def subtract(self, right):
        return Number(self.val - right.val)
    def multiply(self, right):
        return Number(self.val * right.val)
    def divide(self, right):
        return Number(self.val / right.val)

    #all these are simple boolean operations that we have to operate on the Number objects we create
    def equals(self, right):
        result = self.val == right.val
        return Number(result)
    def notEquals(self, right):
        result = self.val != right.val
        return Number(result)
    def greater(self, right):
        result = self.val > right.val
        return Number(result)
    def less(self, right):
        result = self.val < right.val
        return Number(result)
    def greaterEq(self, right):
        result = self.val >= right.val
        return Number(result)
    def lessEq(self, right):
        result = self.val <= right.val
        return Number(result)

#this is the actual Interpreter class that we use to create and instantiate the interpreter when we run the code
#it holds all the possible operations and functions that can be encountered when parsing
class Interpreter:

    #this is a visit function that takes in a parse node and a variable table and returns the method of which node we need
    def visit(self, node, vars):
        name = f'visit_{type(node).__name__}'
        method = getattr(self, name)
        return method(node, vars)

    #this method is called when we reach an IntNode in our parser
    #all it does is return an int value
    def visit_IntNode(self, node, vars):
        #print("int node")
        value = int(node.token.value)
        return Number(value)

    # this method is called when we reach a VarNode in our parser
    # all it does is return an variable value by looking it up in our variable holder
    def visit_VarNode(self, node, vars):
        #print("var node")
        value = vars.get(node.token.value)
        return value

    # this method is called when we reach an endNode in our parser
    # all it does is return the end name
    def visit_endNode(self, node, vars):
        #print("end")
        value = node.token.value
        return Number(value)

    # this method is called when we reach an PrintStatementNode in our parser
    # this method looks at the print expression in our print node and returns its value
    def visit_PrintStatementNode(self, node, vars):
        #print("print statement node")
        expr = node.printExpr
        value = self.visit(expr, vars)
        #according to the grammar of our language a print statement should only return an arithmetic expression so we do not have to worry about quotes since that will return an error anyway
        print(value.val)
        return Number(value.val)

    # this method is called when we reach an IfStatementNode in our parser
    # this method looks at the boolean expression in our if node and returns the value of the expression inside the if statement if it returns true
    def visit_IfStatementNode(self, node, vars):
        #print("if statement node")
        boolState = self.visit(node.exprOne, vars)
        if boolState.val == True:
            value = self.visit(node.exprTwo, vars)
            return Number(value.val)

    # this method is called when we reach an IfElseStatementNode in our parser
    # this method works just like the if node but if the boolean expression returns false we perform the expression in the else statement instead
    def visit_IfElseStatementNode(self, node, vars):
        #print("if statement node")
        boolState = self.visit(node.exprOne, vars)
        if boolState.val == True:
            value = self.visit(node.exprTwo, vars)
            return Number(value.val)
        else:
            value = self.visit(node.exprThree, vars)
            return Number(value.val)

    # this method is called when we reach an WhileStatementNode in our parser
    # this method loops infinitely until the while condition statement returns false. while it is looping it performs all the expressions whithin the while block
    def visit_WhileStatementNode(self, node, vars):
        #print("while statement node")
        while True:
            condition = self.visit(node.boolExpr, vars)

            if condition.val == False:
                break
            for index, i in enumerate(node.doStuff):
                value = self.visit_list(node.doStuff, vars, index)
        return Number(value.val)

    #this is a helper function for our nodes that have a list of expressions to execute rather than just one
    #it helps loop through the list of expressions and returns the value of each one
    def visit_list(self, list, vars, count):
        #print("list")
        node = list[count]
        value = self.visit(node, vars)
        return value

    #this functions catches if it reaches a token variable without hitting any nodes
    #in my testing this only happened with identifier variable so i just checked if the token was an identifier and returned its value
    def visit_Token(self, node, vars):
        #print("Var node")
        #value = 0
        if node.name == "Identifier":
            value = vars.get(node.value)
        return value

    # this method is called when we reach an AssignOpNode in our parser
    # this method handles assigning values to variables by checking what kind of assignment it is (whether =, +=, -=, etc.) and does the appropriate assignment
    def visit_assignOpNode(self, node, vars):
       # print("assignOpNode node")
        var = node.leftNode.value
        assignment = self.visit(node.rightNode, vars)
        eqType = node.EQ

        if eqType.value == "=":
            vars.set(var, assignment)
            return assignment
        if eqType.value == "+=":
            varVal = vars.get(node.leftNode.value)
            assignment = varVal.add(assignment)
            vars.set(var, assignment)
            return assignment
        if eqType.value == "-=":
            varVal = vars.get(node.leftNode.value)
            assignment = varVal.subtract(assignment)
            vars.set(var, assignment)
            return assignment
        if eqType.value == "*=":
            varVal = vars.get(node.leftNode.value)
            assignment = varVal.multiply(assignment)
            vars.set(var, assignment)
            return assignment
        if eqType.value == "/=":
            varVal = vars.get(node.leftNode.value)
            assignment = varVal.divide(assignment)
            vars.set(var, assignment)
            return assignment

    # this method is called when we reach a boolOpNode in our parser
    # this method handles comparing 2 values in a boolean expression. It determines how it compares based on the value of the boolean operator
    def visit_boolOpNode(self, node, vars):
        #print("boolOpNode node")
        leftSide = self.visit(node.leftNode, vars)
        rightSide = self.visit(node.rightNode, vars)
        boolOp = node.boolOp

        if boolOp.value == "==":
            result = leftSide.equals(rightSide)
        if boolOp.value == "~=":
            result = leftSide.notEquals(rightSide)
        if boolOp.value == ">":
            result = leftSide.greater(rightSide)
        if boolOp.value == "<":
            result = leftSide.less(rightSide)
        if boolOp.value == ">=":
            result = leftSide.greaterEq(rightSide)
        if boolOp.value == "<=":
            result = leftSide.lessEq(rightSide)
        return result

    # this method is called when we reach a mathOpNode in our parser
    # this method handles the mathmatical expression between both numbers and variable. The operation performed is determined by the operator of the mathOpNode
    def visit_mathOpNode(self, node, vars):
        #print("math op node")
        leftSide = self.visit(node.leftNode, vars)
        rightSide = self.visit(node.rightNode, vars)

        if(node.op.name == "Addition_Operator"):
            result = leftSide.add(rightSide)
        elif (node.op.name == "Subtraction_Operator"):
            result = leftSide.subtract(rightSide)
        elif (node.op.name == "Multiplication_Operator"):
            result = leftSide.multiply(rightSide)
        elif (node.op.name == "Division_Operator"):
            result = leftSide.divide(rightSide)
        return result

    # this method is called when we reach a FunctionNode in our parser
    # this method handles our functions. It does this by looping through the list of every expression present in the function until everything is done then returning the values
    def visit_FunctionNode(self, node, vars):
        #print("func node")
        for index, i in enumerate(node.everything):
            value = self.visit_list(node.everything, vars, index)
        return Number(value.val)



#here is how we return the results of our parser and use it for the interpreter
parser = Parser(tokens)
done = 0
stopInf = 0

#here is where we create the variable holder for our interpreter
vars = VariableHolder()

#here we create the interpreter object
interpreter = Interpreter()

#here we parse through each part of the file until it is done
#if for some reason it loops too many times we send a last resort error message and break out of the loop
while (done == 0):
    parsed = parser.parse()

    #this uses the interpreter to look through our parsed nodes
    res = interpreter.visit(parsed, vars)

    #here we loop through the file until it it done and return an error if we loop through too many times
    if  parser.tokIdx >= len(tokens):
        done = 1
    if stopInf > 1000:
        print("error in file")
        done = 1
    stopInf += 1



