
# Ask user for second number
# Ask user which operation to perform (Add, Multiply, Subtract, Divide)
# Perform the operation on the two numbers
# Print result to terminal

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==>{message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]


prompt(messages('welcome'))

while True: # Outer While loop to allow for multiple calculations
    # Ask user for first number
    prompt('Please enter your first number:')
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number','en'))
        number1 = input()


    prompt('Please enter your second number:')
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number','es'))
        number2 = input()

    prompt("""What operation would you like to perform?\n
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    while operation not in ['1','2','3','4']:
        # ask again
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case  '4':
            output = float(number1) // float(number2)



    prompt(f'The result is: {output}')
    prompt("Do you want to another calculation? Enter 'Yes' or 'Y'")
    answer = input()

    if answer and answer[0].lower() != 'y':
        prompt('Thank you for using our calculator!')
        break
    
    
   

        
   