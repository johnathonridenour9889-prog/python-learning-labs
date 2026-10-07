def age_check():
    age = input('enter your age')
    age = int(age)

    if age >= 60:
        print('damn you old as fuck')
    elif age >= 21:
        print('come on in')
    else:
        print('go home kid')

while True:
    age_check()