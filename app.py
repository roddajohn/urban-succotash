from flask import Flask, render_template
import random

app = Flask(__name__)

dictionary = dict()
# creates empty dict
class yay():
    name = ""
    percentage = ""
    link = ""

def pick_random():
    random_number = random.random()
    random_number = random_number * 99.8

    # Total is 99.8 pick a random number from 0 to 99.8

    for key in dictionary:
        # Iterate through all the keys, if the random number is less than the value, pick it, if not, iterate to the next, subtract the value of the current from the random_number
        if random_number < dictionary[key]:
            return key
        random_number -= dictionary[key]

@app.route('/a')
def a():
    return 'a'

@app.route('/b')
def b():
    return 'b'

@app.route('/')
@app.route('/occupations')
def hello_world():
    csv = open('occupations.csv').read()
    # open occupations.csv loads the string into variable csv    
    
    for line in csv.split('\n'):
        if not line == "":
            # If there are quotes, make the key the occupation without quotes (careful with commas)
            if line[0] == '"':
                dictionary[line.split('"')[1]] = []
                dictionary[line.split('"')[1]].append(float(line.split('"')[2].split(',')[1]))
                dictionary[line.split('"')[1]].append(line.split('"')[2].split(',')[2])
                # If there are no quotes, don't bother with careful parsing
            else:
                dictionary[line.split(',')[0]] = []
                dictionary[line.split(',')[0]].append(float(line.split(',')[1]))
                dictionary[line.split(',')[0]].append(line.split(',')[2])

    list_to_return = []
    for key in dictionary:
        new_yay = yay()
        new_yay.name = key
        new_yay.percentage = dictionary[key][0]
        new_yay.link = dictionary[key][1]
        list_to_return.append(new_yay)

        
    return render_template('index.html', title = 'Occupations', bl = list_to_return, randomly_selected = pick_random())

if __name__ == "__main__":
    app.debug = True
    app.run()
