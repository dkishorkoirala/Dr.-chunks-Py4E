largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num.lower() == "done":
        break
    
    try:
        num = int(num)
    except ValueError:
        print("Invalid input") 
        continue
    
    if largest is None or num > largest:
        largest = num
    
    if smallest is None or num < smallest:
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)
