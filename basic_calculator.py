

# Function add is in charge of adding
def add(a, b):
    answer = a + b
    print(str(a), "+", str(b), "=", str(answer))

# Function sub is in charge of subtraction
def sub(a, b):
    answer = a - b
    print(str(a), "-", str(b), "=", str(answer))

# Function mult is in charge of multiplication
def mult(a, b):
    answer = a * b
    print(str(a), "x", str(b), "=", str(answer))

# Function div is in charge of division
def div(a, b):
    answer = a / b

    print(str(a), "/", str(b), "=", str(answer))

# Function calc is in charge of welcoming users to the calculator
# and making sure the operation they choose is executed after said
# operation is executed the user is asked if they want to do another 
# operation, if so then the function is called again if not then bye bye
def calc():

    print("Welcome to my Basic Calculator!!!")
    print("Which Basic Operation would you like to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = int(input("Which operation would you like to do: "))

    if operation == 1:
        print("Addition")
        a = int(input("What is your first number? "))
        b = int(input("What is your second number? "))
        add(a, b)

    elif operation == 2:
        print("Subtraction")
        a = int(input("What is your first number? "))
        b = int(input("What is your second number? "))
        sub(a, b)

    elif operation == 3:
        print("Multiplication")
        a = int(input("What is your first number? "))
        b = int(input("What is your second number? "))
        mult(a, b)

    elif operation == 4:
        print("Division")
        a = int(input("What is your first number? "))
        b = int(input("What is your second number? "))
        div(a, b)

    again = str(input("Would you like to do another operation?(Yes or No) "))

    if again.lower() == "yes":
        calc()
    
    if again.lower() == "no":
        print("Goodbye")

calc()