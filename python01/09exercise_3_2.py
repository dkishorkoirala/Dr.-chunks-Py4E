#3.2 Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

strhrs = input("Enter Hours:")
strrate = input("Enter the rate to Pay: ")

try:
    fhrs= float(strhrs)
    frate = float(strrate)
except:
    print("Error, please input numeric input")
    quit()

print(fhrs, frate)

if fhrs > 40:
    reg = fhrs* frate
    otp = (fhrs - 40) * (frate * 0.5)

    pay = reg + otp

else:
    pay = fhrs* frate

print(pay)