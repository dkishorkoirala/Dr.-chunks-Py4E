#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(':')

#print(ipos)

piece = text[ipos+5:]
#print(piece)
#print(piece+42.0) #will fail
value = float(piece)
print(value)
#print (value+42.0)
