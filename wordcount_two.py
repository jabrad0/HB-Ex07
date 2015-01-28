"""Code from Wendy D  --> doubledherin"""

import string
from sys import argv

script, filename = argv

def main():
    hist = {}

    exclude = string.punctuation
    

    fin = open(filename)
    for line in fin:    
        # get rid of punctuation
        line = ''.join(char for char in line if char not in exclude)
        
        # lowercase, dump newlines, and split into a list of word strings
        line = line.lower().rstrip().split(" ")
        
        # build histogram
        for item in line:
            # chuck strings of digits and empty strings
            # if item == "" or item[0] in "0123456789":
            #     continue
            hist[item] = hist.get(item, 0) + 1
    print "This is the original histogram, k,v pairs:"
    print hist
    print " "
    
    # invert histogram, so key = frequency and value = list of words
    inverse = {}
    for key in hist:
        val = hist[key]
        inverse.setdefault(val,[]).append(key)
    print "This is the inverse of the histogram with words grouped in a list:"
    print inverse
    print " "

    # convert inverted histo into list of tuples sorted by descending frequency
    inverse_tuples = sorted(inverse.items(), reverse=True)
    print "Convert k,v pairs to tuples, in descending numeric order:"
    print inverse_tuples
    print " "
    
    # loop through list of tuples, sorting words for each one & printing
    for tuple_ in inverse_tuples:
        words = sorted(tuple_[1])
        for word in words:
            print "%s: %r" % (word, tuple_[0])


if __name__ == "__main__":
    main()