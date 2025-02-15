# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")


try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found:", fname)
    exit()

count = 0
total_confidence = 0.0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        confidence_value = float(line.strip().split(":")[1])
        
        total_confidence += confidence_value
        count += 1

if count > 0:
    average_confidence = total_confidence / count
    print("Average spam confidence:", average_confidence)
else:
    print("No matching lines found.")
