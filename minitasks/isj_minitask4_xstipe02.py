# minitask 4
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
wanted = dict()
for key,val in mcase.items():
    wanted.setdefault(key.lower(), 0)
    wanted[key.lower()] = wanted[key.lower()] + val
print(wanted)
# wanted = {'a': 17, 'b': 34, 'z': 3}