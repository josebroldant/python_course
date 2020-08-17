"""
SOLOLEARN PYTHON COURSE LESSON 5
"""

#MORE TYPES OF VARIABLES

print(None == None)#none is absence of value
def func():
    print("Nothing")
var=func()
print(var)

#DICITONARIES
ages = {"Dave": 24, "Mary": 42, "John": 58}#opened with keys and each data has a key:value format, separated by comas as a list
print(ages["Dave"])
print(ages["Mary"])
#indexing data
primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])

#FUNCTIONS IN DICTIONARIES

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
#asign new data to a position
squares[8] = 64
squares[3] = 9
print(squares)

#determine if an element is a key or not, use statement in
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#get method for indexing
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

#TUPPLES

#lists that cannot be changed (as const in js)
words = ("spam", "eggs", "sausages",)
my_tuple = "one", "two", "three"#another form to write a tuple
print(words[0])

#list slices for better indexing
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])#prints the data in the selcted range
print(squares[3:8])
print(squares[0:1])
print(squares[:7])#start of the list
print(squares[7:])#end of the list
print(squares[::2])#is a two step
print(squares[2:8:3])#can include athird number that is the step (min-range:max-range:step)

#can use negative numbers to ommit elements in the list while counting them

#LIST COMPREHENSIONS

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

#conditioned list
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#wide ranges causes a memory error
#even = [2*i for i in range(10**100)] DONT DO THIS  

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
a = "{x}, {y}".format(x=5, y=12)
print(a)

"""
ANOTHER STRING FUNCTIONS:
Python contains many useful built-in functions and methods to accomplish common tasks.
join - joins a list of strings with another string as a separator.
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
To change the case of a string, you can use lower and upper.
The method split is the opposite of join, turning a string with a certain separator into a list.
Some examples:
"""

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

#NUMERIC FUNCTIONS
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

#more numeric functions
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):#can access indexes and data
   print(v)

#TEXT ANALYSER

#program that finds how much a character is repeated in a file
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "a"))

#what percentage of the text each character of the alphabet occupies.
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)#divides over the length of text that is the read file
  print("{0} - {1}%".format(char, round(perc, 2)))#formats the result rounding it to 2 decimals and using str formating method