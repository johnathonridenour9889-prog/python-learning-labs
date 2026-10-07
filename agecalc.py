def calculate_age():
    try:

        print ('enter your age')

        user_age = input()

        convert_1 = float(user_age)
        age_in_days = (convert_1 * 365)
        print (f'you are {convert_1} years old and {age_in_days} days old.')


    except ValueError:
        print("Please enter a valid number.")

while True:
    calculate_age()



