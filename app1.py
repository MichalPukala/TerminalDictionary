import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]  #special case for proper nouns
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for 'yes', or N for 'no': " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        yn = yn.upper()
        while yn != "Y" and yn != "N":
            yn = input("Query not understood, please type Y for 'yes', or N for 'no': ")
            yn = yn.upper()
            if yn == "Y":
                return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
                break
            elif yn == "N":
                return "The word doesn't exist. Please double-check it."
                break
            else:
                continue
        if yn == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double-check it."
        else:
            return "Query not understood."
    else:
        return "The word doesn't exist. Please double-check it."

word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)