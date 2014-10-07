from sys import argv

def create_word_list(filename):
    #word_list = []

    input_file = open(filename)

    # for line in input_file:
    #     words = line.rstrip().split()
    #     for word in words:
    #         word_list.append(word)

    filetext = input_file.read()
    filetext = filetext.replace('\n', ' ')
    word_list = filetext.split()

    input_file.close()

    for i in range(len(word_list)):
        word_list[i] = remove_punctuation(word_list[i])
        
    return word_list

def remove_punctuation(word):
    punctuation = '.?!,""'
    new_word = ""
    for char in word:
        if char not in punctuation:
            new_word = new_word + char
    return new_word.lower()



def create_dictionary(word_list):
    word_count = {}

    for item in word_list:
        word_count[item] = word_count.get(item, 0) + 1
        # if item in word_count:
        #     word_count[item] += 1
        # else:
        #     word_count[item] = 1

    return word_count


def print_dictionary(dictionary):
    for k, v in dictionary.iteritems():
        print k, v

def main():
    filename = argv[1]

    word_list = create_word_list(filename)
    word_dict = create_dictionary(word_list)
    print_dictionary(word_dict)

if __name__ == "__main__":
    main()