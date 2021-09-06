import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate():

    word = input("Enter word: ").lower()

    if word in data:
        return data[word]
    elif word.capitalize() in data.keys():
        return data[word.capitalize()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Yes or No: ")

        if yn[0].lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn[0].lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"

    else:
        return "The word doesn't exist. Please double check it."


output = translate()

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
