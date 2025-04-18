name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

hours_count = dict()

for line in handle:
    if line.startswith("From "):  # Only consider lines that start with "From "
        words = line.split()
        time = words[5]  # time is at index 5 (e.g., 09:14:16)
        hour = time.split(':')[0]  # extract the hour part
        hours_count[hour] = hours_count.get(hour, 0) + 1

# Sort by hour
for hour, count in sorted(hours_count.items()):
    print(hour, count)
