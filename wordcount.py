from sys import argv

script, filename = argv

word_list = []

input_file = open(filename)

for line in input_file:
    words = line.rstrip().split(" ")
    for word in words:
        word_list.append(word)

input_file.close()

print word_list
