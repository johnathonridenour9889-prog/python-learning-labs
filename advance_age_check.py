def _ask_user_age():
    try:
        return int(input("Enter your age: "))
    except ValueError:
        print("Please enter your age.")
        return None

def _internal_age_check():
        user_age = _ask_user_age()

        if user_age is None:
            return

        if 18 <= user_age <21:
            print("You can enter but you can not drink and will be stamped")
        elif user_age < 18:
            print("You can not enter you are under age")
        else:
            print("You can enter you are 21 or older")

while True:
    _internal_age_check()
