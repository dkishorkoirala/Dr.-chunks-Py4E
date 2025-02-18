#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)

# Dictionary to store email counts
many = dict() 

for line in fhand:
    line = line.rstrip()

    # Ignore lines that don't start with 'From '
    if not line.startswith("From "):  
        continue

    wds = line.split()
    # Extract the sender's email
    email = wds[1]  
     # Count occurrences
    many[email] = many.get(email, 0) + 1 

largest = None
bigword = None

for key, value in many.items():
    if largest is None or value > largest:
        largest = value
        bigword = key

print(bigword, largest)


