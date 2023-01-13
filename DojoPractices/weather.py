import time
import re
db = [
    {
        'id': 1,
        'city':'Valley Stream',
        'zipcode':'11581',
        'state':'New York',
        'temp':'67',
        'precip':'rain',

        'created_at':'2000-12-1',
        'updated_at':'2023-12-1'
    },

    {
        'id': 3,
        'city':'Winchester',
        'zipcode':'01890',
        'state':'MA',
        'temp':'42.8',
        'precip':'rain',

        'created_at':'2000-12-1',
        'updated_at':'2023-12-1'
    },

    {
        'id': 2,
        'city':'Port Richey',
        'zipcode':'34668',
        'state':'Florida',
        'temp':'61',
        'precip':'light Humidity',

        'created_at':'2000-12-1',
        'updated_at':'2023-12-1'
    },

    {
        'id': 4,
        'city':'San Antonio',
        'zipcode':'78220',
        'state':'Texas',
        'temp':'63',
        'precip':'light rain',

        'created_at':'2000-12-1',
        'updated_at':'2023-12-1'
    }
]

print(db[0])

count = 0
def myBot():
    # The bot will take in an input and return the information that was asked of it.
    # The bot takes in a db, then it asks the user for an input.
    # it will take the input and try to find it in the db
    # if found it, will return the results; otherwise, it will return not found
    global count, db
    if count < 1:
        print("Do you want to know the weather of a specific city?")
        user_input = input()
    else:
        print("Do you want to know the weather of another city?")
        user_input = input()

    if re.match('^y', user_input):
        print('What city would you like to see?')
        city = []
        for data in db:
            city.append(data['city'])
        print(f"Here's some options: {city}")
        user_input = input()
        for data in db:
            if user_input == data['city']:
                print(f"The temperature in {data['city']} is {data['temp']} and the precipitation is {data['precip']} !")
                time.sleep(2)
                myBot()
    elif re.match('^n', user_input):
        print("Aright then")
    else:
        print("Not sure what you mean")

myBot()
