#add
def add(n1,n2):
    return n1 + n2

#sub 
def sub(n1,n2):
    return n1 - n2
#mul
def mul(n1,n2):
    return n1 * n2
#div 
def div(n1,n2):
    return n1 /n2

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

for key in operations:
    print(key)
looping = True
num1 = int(input("enter first value : "))
while looping:
    operation = input("enter operation : ")
    calculate = operations[operation]
    num2 = int(input("enter second value : "))
    first_answer = calculate(num1,num2)
    print(f"{num1} {operation} {num2} = {first_answer}") 
    response = input("continue 'y' or no 'n'")
    if response == 'y':
        num1 = first_answer
    else:
        looping = False
    #expression = input("enter expression :")
    #num3 = int(input("enter next digit "))
    #calculate = operations[expression]
    #second_answer = calculate(first_answer,num3)
    #print(second_answer)