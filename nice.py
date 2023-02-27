import json, pprint

import random

with open('./out.json') as file:
    data: dict[dict[str, int]] = json.load(file)

out = {}
for letter in data:
    total = sum(data[letter].values())
    new = {}
    for key, val in data[letter].items():
        new[key] = val / total
    out[letter] = new

pprint.pprint(out)