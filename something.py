import random

csv = open('occupations.csv').read()
# open occupations.csv loads the string into variable csv

dictionary = dict()
# creates empty dict

for line in csv.split('\n'):
    if not line == "":
        # If there are quotes, make the key the occupation without quotes (careful with commas)
        if line[0] == '"':
            dictionary[line.split('"')[1]] = float(line.split('"')[2].split(',')[1])
        # If there are no quotes, don't bother with careful parsing
        else:
            dictionary[line.split(',')[0]] = float(line.split(',')[1])

def pick_random():
    random_number = random.random()
    random_number = random_number * 99.8

    # Total is 99.8 pick a random number from 0 to 99.8

    for key in dictionary:
        # Iterate through all the keys, if the random number is less than the value, pick it, if not, iterate to the next, subtract the value of the current from the random_number
        if random_number < dictionary[key]:
            return key
        random_number -= dictionary[key]

print pick_random()

