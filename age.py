import datetime

'''
    Function to calculate the age of a person given their birthday and the current date.
'''
def calculate_age(birthday): 
    # 
    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')

    # Get the current date dynamically. 
    current = datetime.datetime.now()
    
    # Subracting year attributes from both instances to find age. 
    age = current.year - birthday.year

    # The current age calculation already accounts for the person's birthday this year, 
    # so we need to check for whether the person's birthday this current year has 
    # truly happened yet or not. 
    if (birthday.month, birthday.day) > (current.month, current.day): 
        age -= 1 # Decrement the age by 1 if the birthday hasn't happened yet this year.

    return age 



''' 
Seperate function for getting the birthday input from the user, 
    with error handling for incorrect YYYY-MM-DD formats.
'''
def get_birthday():
    while True: 
        try: 
            birthday_input = input('Please provide your birthday in this format (YYYY-MM-DD): ')

            # Parsing the input string into a datetime object
            birthday = datetime.datetime.strptime(birthday_input, '%Y-%m-%d')
            return birthday
        # As input() will always return a string, we won't be having any type erros breaking out loop
        # instead, the incorrect format for .strptime() is what leads to any ValueErrors. 
        except ValueError: 
            print('Invalid format. Please enter the date in the format YYYY-MM-DD')

if __name__ == '__main__': 
    print('')
    print('')

    print('Welcome to the SigmaLabs age calculator!')
    print('')

    birthday = get_birthday()
    age = calculate_age(birthday)

    print('')
    print(f'You are {age} years old.')
