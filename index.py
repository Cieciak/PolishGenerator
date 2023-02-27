import json

with open('./slowa.txt') as file:
    slowa = file.readlines()

total = ''.join(slowa)

p = {}
for a in 'aąbccdeerfghijklłmnńoprsśtuwyzźż':
    t = {}
    for i in 'aąbccdeerfghijklłmnńoprsśtuwyzźż':
        t[i] = 0
    p[a] = t

print('Ilość:', len(total))
print(p)
for index, letter in enumerate(total):
    try: p[letter][total[index+1]] += 1
    except: pass
print(p)
