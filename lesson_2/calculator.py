
# Ask user for second number
# Ask user which operation to perform (Add, Multiply, Subtract, Divide)
# Perform the operation on the two numbers
# Print result to terminal

def prompt(message):
    print(f'==>{message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

# Ask user for first number
prompt('Please enter your first number:')
number1 = input()

while invalid_number(number1):
    prompt("Hmm...that doesn't look like a valid number. Please try again.")
    number1 = input()


prompt('Please enter your second number:')
number2 = input()

while invalid_number(number2):
    prompt("Hmm...that doesn't look like a valid number. Please try again.")
    number2 = input()

prompt("""What operation would you like to perform?\n'
1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ['1','2','3','4']:
    # ask again
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case  '4':
        output = int(number1) // int(number2)



prompt(f"The result is: {output}")