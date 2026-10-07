
def __tweet__():
    tweet = input('enter your tweet')
    max_char = 10
    char_count = len(tweet)
    if char_count < max_char:
        print('tweet sent')
    else:
        print(f'tweet not sent {char_count} characters tweet is '
              f'{char_count - max_char} characters too long')

while True:
    __tweet__()