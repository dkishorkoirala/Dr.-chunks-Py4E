#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


strhrs = input("Enter Hours:")
strrate = input("Enter the rate to Pay: ")
fhrs= float(strhrs)
frate = float(strrate)
#print(fhrs, frate)

if fhrs > 40:
    #print("Overtime")
    reg = fhrs* frate
    otp = (fhrs - 40) * (frate * 0.5)
   # print(reg,otp)
    pay = reg + otp

else:
    #print("regular")
    pay = fhrs* frate

print(pay)