import random

print ('choose a number between blank and blank ill make a random number')

def _user_ranom_number():
    try:
        user_1 = int(input('enter first number:'))
        user_2 = int(input('secound number:'))

        number = random.randint(int(user_1), int(user_2))

        number_chose = (f"The random number is {number}")
        print (number_chose)

    except ValueError:
        print('pls enter valid number')

while True:
    _user_ranom_number()