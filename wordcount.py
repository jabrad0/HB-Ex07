from sys import argv

script, filename = argv

word_list = []

input_file = open(filename)

for line in input_file:
    words = line.rstrip().split(" ")
    for word in words:
        word_list.append(word)

input_file.close()

word_count = {}

for item in word_list:
    if word_count.get(item):
        word_count[item] += 1
    else:
        word_count[item] = 1

for k, v in word_count.iteritems():
    print "%s %d" % (k, v)