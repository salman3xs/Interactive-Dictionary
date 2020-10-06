import json
import difflib

data = json.load(open('data.json'))


def trans(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(difflib.get_close_matches(w, data.keys())) > 0:
        a = input('Did u mean %s?\n Y=YES/N=NO:'%difflib.get_close_matches(w, data.keys())[0])
        if a == 'y':
            return data[difflib.get_close_matches(w, data.keys())[0]]
        else:
            return 'search again'
    else:
        return 'word not found'


x = input('Enter word:')
output = (trans(x))
if type(output) == list:
    n = 1
    for z in output:
        print(n, z)
        n += 1
else:
    print(output)
