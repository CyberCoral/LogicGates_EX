import numpy as np

# I import math because I need the log function
from math import ceil, floor

# These program will be about logic gates based on functions instead of python's
# key works. I hope it's useful in some way or another

################

# Useful Programs #

################

###
### This program makes a truth list out of a binary string of characters (made of 0s and 1s)
###

def BinaryCounter(binary):
    '''
    This program works as a homemade
    binary number counter, only going up.
    '''
    if isinstance(binary, str) != True:
        raise TypeError("Invalid type for a binary number")
    elif [True if binary[i] in ['0','1'] else False for i in range(len(binary))].count(False) > 0:
        raise SyntaxError("Invalid characters (not 0 or 1) in string.")
    
    bi = ""
    i = len(binary) - 1
    
    if binary.count("1") == len(binary):
        return "1" + "0"*len(binary)
    
    while i < len(binary):
        if binary[i] == "0":
            bi += "1"
            break
        else:
            bi += "0"
        i -= 1
        
    return binary[:i] + bi[::-1]

def BinaryToTruthList(binary):
    '''
    This program returns a list consisted of
    Truth and False based on a string of
    ONLY 0s and 1s (if this rule is broken, the
    program will return a SyntaxError).
    '''
    binary = str(binary)
    try:
        binary = [int(i) for i in binary]
    except ValueError:
        raise SyntaxError("{} is an invalid string from which to create a truth list.".format(binary))
    truth_list = []
    for j in range(len(binary)):
        if binary[j] not in [0,1]:
            raise SyntaxError("{} is an invalid character of a binary string.".format(binary[j]))
        else:
            truth_list.append(bool(binary[j]))
    return truth_list
            
###
### This program will be used to check common variable types
###

def ErrorTypeFinder(var, conditions, or_: bool = False):
    '''
    This program checks for variable's type
    according to conditions' truth values.
    The order of validation is this one:
    int -> float -> complex -> tuple
    -> list -> dict.         (str)
    
    Any other more input will not be considered.
    If there are less than 6 inputs, all the other
    ones are False by default, except with str.
    In that case, you have the max of 7 inputs
    '''
    dict_condition = {}
    condition = ["int","float","complex","tuple","list","dict","str"]

    if isinstance(conditions, list) != True:
        return ErrorTypeFinder(conditions,BinaryToTruthList("000010"))
    
    for i in range(len(conditions)):
        if isinstance(conditions[i], bool) != True:
            raise SyntaxError("The conditions' value ({}) type ({}) is invalid.".format(conditions[i], type(conditions[i])))

    if len(conditions) <= len(condition):
        for i in range(len(condition) - len(conditions)):
            conditions.append(False)
    elif len(conditions) >= len(condition):
        conditions = conditions[0:len(condition)]
        
    if conditions.count(True) > 1 and or_ == False:
        raise SyntaxError("A variable cannot be two types at the same time.")
    elif conditions.count(False) == len(conditions):
        raise SyntaxError("There has to be a condition that is met.")

    elif isinstance(var, str) != True and len(conditions) >= 7:
        if conditions.index(True) == 6:
            raise TypeError("{} is supposed to be {}".format(var, str))
        else:
            del conditions[6]
    elif isinstance(var, str) == True and len(conditions) >= 7:
        if conditions.index(True) == 6:
            return True
    elif isinstance(var, str) == True and len(conditions) < 7:
        raise TypeError("{} is supposed to be {}, but cannot be valued because of conditions' setting.".format(var, str))
    else:
        del conditions[6]

    if len(conditions) <= len(condition):
        for i in range(len(condition) - len(conditions)):
            conditions.append(False)
    elif len(conditions) >= len(condition):
        conditions = conditions[0:len(condition)]
        
    for j in range(len(condition)):
        dict_condition.update({condition[j]: conditions[j]})

    conditions = []
    
    for k in range(len(condition)):
        
        # 1er error: conditions.append("if (lambda var, k, condition, dict_condition: False if isinstance(var, condition[k]) != dict_condition[condition[k]] else True)"+f"({var},{k},{condition},{dict_condition}) == False: raise TypeError('Type of {var} is not {condition[k]}')")
        # 2do error: conditions.append(f'if isinstance({var}, {condition[k]}) != {dict_condition[condition[k]]}: raise TypeError("Type of {var} is not {condition[k]}")')

        conditions.append(f"""if (lambda var, k, condition, dict_condition: False if isinstance(var, eval(condition[k])) != dict_condition[condition[k]] else True)({var},{k},{condition},{dict_condition}) == False:  raise TypeError('''Type of {var} is supposed to be {type(var)}''')""")
        exec(compile(conditions[0],"<string>","exec"))
        del conditions[0]

    return True

 
##################

# Basic Logic Gates #

##################

# This lambda is used a lot here

lambdacheck = lambda i: False if isinstance(i, bool) != True else True

# Returns input
def buffer(A: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    return A

# Returns negative input.(also named "inverter")
def Not(A: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    if A == True:
        return False
    else:
        return True

# Returns True if A and B are True, else it returns False
def And(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if A == False:
        return False
    elif B == False:
        return False
    else:
        return True

# Negative equivalent of And
def Nand(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    
    if A == True:
        return False
    elif B == True:
        return False
    else:
        return True

# Returns True if A or B are True, including A and B are True, else it returns False
# Inclusive Or
def Or(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if A == True:
        return True
    elif B == True:
        return True
    else:
        return False

# Negative equivalent of Or
def Nor(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if A == False:
        return True
    elif B == False:
        return True
    else:
        return False

# Returns True if A or B are True, but if A and B are True or False it returns False
# Exclusive Or
def Xor(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if And(A,B) == True:
        return False
    if A == True:
        return True
    elif B == True:
        return True
    else:
        return False 
# Negative equivalent or Xor
def Xnor(A: bool, B: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if And(A,B) == True:
        return True
    if A == True:
        return False
    elif B == True:
        return False
    else:
        return True

# If Select is true it returns A, else it returns B.
def Mux(A: bool, B: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(Select) == True:
        raise(TypeError("Type of element",Select,"is not valid.",Select,"is not valid."))

    if Select == True:
        return B
    else:
        return A

# Negative equivalent of Mux
def Nmux(A: bool, B: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(Select) == True:
        raise(TypeError("Type of element",Select,"is not valid.",Select,"is not valid."))
    
    if Select == True:
        return A
    else:
        return B

# It puts the input in either channel depending of Select
def Demux(A: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(Select) == True:
        raise(TypeError("Type of element",Select,"is not valid.",Select,"is not valid."))
    
    if Select == True:
        return A, False
    else:
        return False, A

# Negative equivalent of Demux
def NDemux(A: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(Select) == True:
        raise(TypeError("Type of element",Select,"is not valid.",Select,"is not valid."))
    
    if Select == True:
        return False, A
    else:
        return A, False

#######################################################

# Extending the definition of Logic Gates / Advanced Logic Gates #

######################################################

##### AND type #####

# List used for testing
lista= [True, True, True]
lista = list(lista); nlista = len(lista)

# Evaluates AND but for three inputs
def TriAND(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    
    if A == False:
        return False
    elif B == False:
        return False
    elif C == False:
        return False
    else:
        return True

# Negative equivalent of TriAND
def TriNAND(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    
    if A == False:
        return True
    elif B == False:
        return True
    elif C == False:
        return True
    else:
        return False

# Evaluates AND but for any number of inputs
def N_AND(A: bool, B: list):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    if A == False:
        return False
    for i in range(0,len(B)):
        if lambdacheck(B[i]) == True:
            raise(TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        elif i == False:
            return False
    else:
        return True

# Negative equivalent of N_AND
def N_NAND(A: bool, B: list):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    if A == False:
        return True
    
    for i in range(0,len(B)):
        if lambdacheck(B[i]) == True:
            raise(TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        elif i == False:
            return True
    else:
        return False

##### OR Type #####

# Evaluates OR for three inputs
def TriOR(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    
    if A == True:
        return True
    elif B == True:
        return True
    elif C == True:
        return True
    else:
        return False

# Negative equivalent of TriOR
def TriNOR(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    
    if A == True:
        return False
    elif B == True:
        return False
    elif C == True:
        return False
    else:
        return True

# Evaluates OR but for any number of inputs
def N_OR(A: bool, B: list):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    if A == True:
        return True
    for i in range(0,len(B)):
        if lambdacheck(B[i]) == True:
            raise(TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        if i == True:
            return True
    else:
        return False

 # Negative equivalent of N_OR   
def N_NOR(A: bool, B: list):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    if A == True:
        return False
    
    for i in range(0,len(B)):
        if lambdacheck(B[i]) == True:
            raise(TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        if i == True:
            return False
    else:
        return True

##### XOR Type #####

# Evaluates XOR for three inputs
def TriXOR(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    

    if TriAND(A,B,C) == True:
        return False
    elif A == True:
        return True
    elif B == True:
        return True
    elif C == True:
        return True
    else:
        return False

# Negative equivalent of TriOR
def TriXNOR(A: bool, B: bool, C: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    

    if TriAND(A,B,C) == True:
        return True
    elif A == True:
        return False
    elif B == True:
        return False
    elif C == True:
        return False
    else:
        return True

# Evaluates XOR for any number of inputs
def N_XOR(A: bool, B: list):
    B.append(int(A))
    for i in range(0,len(B)):
        if And(lambdacheck(B[i]),((lambda i: False if Or(i == 1, i == 0) else True) (B[i]) )) == True:
            raise (TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        B[i] = int(B[i])
    print(sum(B),"vs",len(B))
    if And((lambda B: True if sum(B) == len(B) else False) (B) , (lambda A: True if A == True else False)(A) ) == True:
        return False
    elif A == True:
        return True
    else:
        return False

# Negative equivalent of N_XOR
def N_XNOR(A: bool, B: list):
    B.append(int(A))
    for i in range(0,len(B)):
        if And(lambdacheck(B[i]),((lambda i: False if Or(i == 1, i == 0) else True) (B[i]) )) == True:
            raise (TypeError("Type of element",B[i],"is not valid.",B,"is not valid."))
        B[i] = int(B[i])
    print(sum(B),"vs",len(B))
    if And((lambda B: True if sum(B) == len(B) else False) (B) , (lambda A: True if A == True else False)(A) ) == True:
        return True
    elif A == True:
        return False
    else:
        return True

listtrue = [True,True]

    
# Evaluates Mux but with three inputs (minimum elements of Select: 2)
def TriMUX(A: bool, B: bool, C: bool ,Select: list == [True, True]):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    

    x2 = len(Select)
    for i in range(0,x2):
        if (lambda i: False if isinstance(Select[i]),bool) == True else True)(i) == True:
            raise( TypeError("Type of element",Select[i],"is not valid.",Select,"is not valid.") )
    if (lambda Select: False if 3 <= 2**len(Select) -1 else True)(Select) == True:
        raise( IndexError("Number of inputs (3) is higher than",Select,"nº of possible outputs") )    
    elif And((lambda Select: True if Select[0] == True else False)(Select), (lambda Select: True if Select[1] == True else False)(Select)) == True:
        return A        
    elif Or((lambda Select: True if Select[0] == True else False)(Select), (lambda Select: True if Select[1] == True else False)(Select)) == True:
        return B
    else:
        return C

# Negative equivalent of TriMUX
def TriNMUX(A: bool, B: bool, C: bool ,Select: list == [True, True]):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))
    elif lambdacheck(C) == True:
        raise(TypeError("Type of element",C,"is not valid.",C,"is not valid."))
    
    x2 = len(Select)
    for i in range(0,x2):
        if (lambda i: False if isinstance(Select[i]),bool) == True else True) == True:
            raise( TypeError("Type of element",i,"is not valid.",Select,"is not valid.") )
    if (lambda B, Select: True if 3 > 2**len(Select) -1 else False) == True:
        raise IndexError( ("Number of inputs (3) is higher than",Select,"nº of possible outputs") )     
    elif And((lambda Select: True if Select[0] == False else False)(Select), lambda Select: True if Select[1] == False else False) == False:
        return A        
    elif Or((lambda Select: True if Select[0] == False else False)(Select), (lambda Select: True if Select[1] == False else False)(Select)) == False:
        return B
    else:
        return C

# Evaluates MUX but for any number of inputs (minimum elements of Select per 2 elements of
# B: 1, minimum elements of B: 2).
Elements = [0,1,2,3,4,5,6,7,8,False,True]

def N_MUX(A: bool, B: list, Select: list):
    Select.insert(0, A)
    x1 = len(Select)
    x2 = len(B)
    print("Nº of elements in B:",x2,"and elements in B: ",B,"\n Nº of elements in Select:",x1,
          "\nIs the number of elements in B greater than the outputs of Select?", x2 > (2**x1)+1)
    for i in range(0,x1):
        if ((lambda i: False if ErrorTypeFinder(Select[i], BinaryToTruthList(1), True) == True else True) (i)) == True:
            raise( TypeError("Type of element",Select[i],"is not valid.",Select,"is not valid.") )
    if (lambda x1, x2: True if x2 > (2**x1) +1 else False)(x1, x2) == True:
        raise( IndexError(B,"nº of elements is higher than",Select,"nº of possible outputs") )
    
    Select = Select[::-1]
    Select = "".join(["0" if Select[i] == False else "1" for i in range(len(Select))])
    counter = "0"*len(Select)
        
    for j in range(0,2**len(Select)):
        if j >= len(B):
            return B[j - 1]
        elif counter == Select:
            return B[j]
        counter = BinaryCounter(counter)

# It puts the input in either channel depending of Select
def Demux(A: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(B) == True:
        raise(TypeError("Type of element",B,"is not valid.",B,"is not valid."))

    if Select == True:
        return A, False
    else:
        return False, A
    
# Negative equivalent of Demux
def NDemux(A: bool, Select: bool):
    if lambdacheck(A) == True:
        raise(TypeError("Type of element",A,"is not valid.",A,"is not valid."))
    elif lambdacheck(Select) == True:
        raise(TypeError("Type of element",Select,"is not valid.",Select,"is not valid."))
    
    if Select == True:
        return False, A
    else:
        return A, False
