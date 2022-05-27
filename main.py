import re  # Import the regex module 


def read_file_content(filename):
    with open(filename, 'r') as fhand:
        content = fhand.read()
    
    return content 


def count_words():
    text = read_file_content("./story.txt")
    # make all letters lowercase
    txt = text.lower()  
    
    # Eliminate punctuations using a regex.
    # Anything that isnt a word(alphanumeric) or a whitespace will be replaced with an empty string.
    new_txt = re.sub(r'[^\w\s]', '', txt)

    counter = {}  # a dictionary with key: word in textfile and value: value count of word.
    for i in new_txt.split():
        counter[i] = counter.get(i, 0) + 1 
        # Gets the value of each key. The value is the word count
        # if the word is not in counter.keys(), .get() assigns a default value of 0 and then '+1' serves as the increment.
        # Depending on how many times the word occurs in the string.
 
    return counter


