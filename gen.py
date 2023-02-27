import json, random

with open('nice.json') as file:
    data = json.load(file)

def generate_word(n, seed):
    for i in range(n):
        seed += random.choices(list(data.keys()), list(data[seed[i]].values()))[0]
    return seed


for _ in range(40):
    print(generate_word(6, random.choice('aąbccdeerfghijklłmnńoprsśtuwyzźż')))
