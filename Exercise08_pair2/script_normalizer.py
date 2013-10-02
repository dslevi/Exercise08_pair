import sys

script, input_file = sys.argv

f = open(input_file)
for x in range(50):
    line = f.read()
    for word in line:
        if ord(word[0]) == 9:
            print line

f.close()

# output_file = open(output_file, 'w')

# script = ""




# for word in text:
#     count = 0
#     for char in word:
#         if char >= ord("A") and char <= ord("Z"):
#             count += 1
#     if count <= 1:
#         script.append(word)

# output_file.write(script)
# output_file.close()

