import sys

script, input_file = sys.argv

f = open(input_file)

new_text= ""
for x in range(len(input_file)):
    line = f.readline().strip()
    print line
    words = line.split(":")
    print words
    for word in words:
        if word == "George Michael":
            new_text.append(words[2])

print new_text
