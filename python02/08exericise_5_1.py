#wap which repeatedly reads number wntil the user enters "done". once "done" is entered, print out the total, count, and average of the number. if the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

num = 0
tot = 0.0

while True :
    sval = input('Enter a number : ')
    if sval == 'done' : 
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('All Done')
print(tot,num,tot/num)