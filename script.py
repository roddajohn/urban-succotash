blah = open('occupations.csv').read()

new_thing = ''

for line in blah.split('\n'):
    if '"' in line:
        new_thing += line + ',www.bls.gov/ooh/' + line.split('"')[1].replace(',', '-').replace(' ', '-').replace('--', '-').lower() + '/home.htm' + '\n'
    else:
        new_thing += line + ',www.bls.gov/ooh/' + line.split(',')[0].replace(' ', '-').lower() + '/home.htm' + '\n'

open('occupations.csv', 'w').write(new_thing)
