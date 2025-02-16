han = open('mbox-short0.txt')

for line in han:
    line = line.rstrip()
    # print('line: ', line)

    # if line == '':
    #     print('Skip Blank')
    #     continue

    wds = line.split()
    # print('words: ', wds)
    
    #gardian pattern a bit stronger with compound statement
    
    if len(wds) < 3 or wds[0] != 'From':
        # print('Ignore')
        continue
    print(wds[2])