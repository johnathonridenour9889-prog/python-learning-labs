def how_fat_is_you():
    try:
        user_high = float(input('How tall are you in inch?'))
        user_weight = float(input('How much do you wigh in lb?'))

        bmi = user_weight * 703 / (user_high ** 2)
        print(f'your bmi is {bmi}')

        if bmi < 16:
            print("Severely underweight")
        elif bmi <= 18:
            print("Underweight")
        elif bmi <= 24:
            print("Normal")
        elif bmi <= 29:
            print("Overweight")
        elif bmi <= 39:
            print("Obese")
        else:
            print("Extremely obese")




    except ValueError:
        print('Please enter numberS.')

while True:
    how_fat_is_you()
