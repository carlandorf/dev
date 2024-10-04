def addition(num_1, num_2):
    add_total = num_1 + num_2
    return add_total
def subtraction(num_1, num_2):
    sub_total = num_1 - num_2
    return sub_total
def multiplication(num_1, num_2):
    multi_total = num_1 * num_2
    return multi_total
def division(num_1, num_2):
    div_total = num_1 / num_2
    return div_total
    
prompt_1 = ("""
_______________________________________________________________________________________________
Welcome to the Simple Python Calculator!------------------------------------------------------- 
Here's how this is going to work, you will be prompted to enter the first number followed by the
arithmetic operation (addition: +, subtraction: -, multiplication: *, division: /)---------------
and finally, you'll enter in the second number.------------------------------------------------
Example:
3
*
3
Your total is: 9.0! 
_______________________________________________________________________________________________
""")
calculate = True

while calculate == True:
    num_1 = input("Please enter the first number: \n")
    arith = input("Please enter the operator: \n")
    num_2 = input("Please enter the second number: \n")
    if arith == "+":
        print(addition(float(num_1), float(num_2)))
    cont = input("Would you like to calculate something else? (y/n)")
    if cont == "y":
        calculate = True
    else:
        calculate = False



