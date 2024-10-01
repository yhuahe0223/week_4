#Emily Wawrzyniak


# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = '
magic= 'abracadabra'
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
print (magic[4])
print (magic [-3])
print (magic.find('c'))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet= 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
#print (alphabet.find ('hij'))
print (alphabet [7:10])
print (alphabet [0:13:2])
print (alphabet [::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote 
quote= "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
print(quote.find ("John F. Kennedy"))
print (quote [83:-1])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info= "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print (info.find('subjective'))
print (info[36:46])

word =info.split()
split_info =['Python', 'is', 'fun.', 'Fun', 'is', 'good.', 'Good', 'is', 'subjective.']
third_word=split_info [::3]
resault =' '.join(third_word)
print(resault)

join_info=split_info [::-1]
resault2= ' '.join(join_info)
print(resault2)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
star="MAY THE FORCE BE WITH YOU."
print(star.lower())


# String Joining and Splitting:
# Given the list motto = 
list1= ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
together_list1 = " ".join(list1)
print (together_list1)

split_list1= together_list1.split('a')
print (split_list1)

# Replacing Words:
# Modify the sentence: 
sentence= "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
new_sentence = sentence.replace("busy","distracted").replace("plans","mistakes")
print(new_sentence)


# Problem Set 4: String Properties and Advanced Operations
# Repetition: ([variable] *15)
# Concatenate the word "Iteration" 7 times.
word2= "iteration"
print (word2 * 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: 
moonlight= "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print (moonlight.find ('moonlight'))
moonlight_found= False

# Length and Count:
super= "Supercalifragilisticexpialidocious"
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase:
# b. Count the number of times the letter 'i' appears in the same word/phrase.
print (len(super))
print (super.count('i'))


##sets are useful when you want to store a 
    #collection of items that should not be chnaged 
    #and you do not care about the order of the items 
    # example: a collection of unique of items 
sS_numbers = {123456789, 987654321, 14689986 }
# remove the last element in this set 
#   print(sS_numbers.pop())

################################################################################
#tuples are immutable and are defined using parenteses 
#   create a tuple called my_tuple with the following values :
example_tuple = (1,2,3,4,5,6,7,8,9,10)
print(example_tuple)
print(example_tuple.count(2))#count the number of times 
#the value 2 appears in the tuple 
print(len(example_tuple))# number of elements in the tuple
print(2 in example_tuple)# check if an element as in the tuple 
#when are they useful
#useful when you want to 

print(example_tuple.index(2))
lymeric = "peter pipe picked a peck of pickled peppers peppers "
#   convert the string to a string 
#   split it first 
lymeric_tupole = tuple(lymeric.split ( ))
print(lymeric_tupole)
## find how many timed yjr the word "peck" appears in the tuple 
#print (lymertic _tuple.count)

#loops with tuple 
for item in example_tuple:
    print(item)

#########################DICTIONARY############################
    #dictionary are un-ordered,changable, indexed 
        #they are defined using curl brackets 
        