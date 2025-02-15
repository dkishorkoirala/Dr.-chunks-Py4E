#Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
fh = open('mbox-short.txt')
for line in fh:
    ly = line.rstrip()
    print (ly.upper())

