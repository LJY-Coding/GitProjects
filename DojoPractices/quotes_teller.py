from quotes import results
import time
import random
import re 
count = 0

# my_list = ["y", "yes", "yea"]

def tellquotes():
    quote = random.choice(results)
    global count

    if count < 1 :
        print("Do you want to hear a good quote?")
    else:
        print("Do you want to hear another quote?")
    user_input = input()

    if re.match('^y', user_input.lower()):
        print(f"Here's the quote: \n {quote['text']}")
        time.sleep(3)
        if quote['author']:
            print(f"Its author is: \n {quote['author']}")
        else:
            print("No author")
        time.sleep(3)
        print("Lolololol")
        count += 1
        tellquotes()
    elif re.match('^n', user_input.lower()):
        print("Awww alright then...")
    else:
        print("Oopps")


tellquotes()