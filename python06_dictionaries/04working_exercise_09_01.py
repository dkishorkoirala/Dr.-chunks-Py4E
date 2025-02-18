fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()
for line in fhand:
    line = line.rstrip()

    wds = line.split()

    for w in wds:
        # print('=====>',w)
        # print('before', many)
        many[w] = many.get(w,0) + 1
        # print('after', many)
# print(many)

#find the word with the largest count

largest = None
bigword = None
for key, value in many.items():
    # print(key, value)
    if largest is None or value > largest:
        largest = value
        bigword = key

print( bigword ,largest)

