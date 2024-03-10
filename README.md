## Python 3 Notebooks:
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp

## Data Types
* Tuples tup - ordered immutable: (10, "hello", 200.3)
* Sets set - unordered collection of unique elements: {1,2,3}

## Slicing
[start:stop:step]
mystring = ['abcdefghijk']
mystring[2] // 'c'
mystring[2:] // 'cdefghijk'
mystring[:3] // 'abc' --> the 3rd index is not included
mystring[3:6] // 'def'
mystring[::2] // 'acegik'
mystring[::-1] // 'kjihgfedcba' --> reverse string

## String Methods
String are immutable, so you can't reassign a character in a string

letter = 'z'
letter * 10 // 'zzzzzzzzzz'

format floating point numbers
"{value:width.precision f}".format(value)
result = 100/777
print("The result was {r:1.3f}".format(r=result))

## Lists
mylist = ['one', 'two', 'three']
mylist.pop() // 'three'
mylist.pop(1) // 'two'
mylist is now ['one']
mylist.append('new item') // ['one', 'new item']
mylist.sort() // ['new item', 'one'] --> in place
sorted(mylist) // ['new item', 'one'] --> not in place
mylist.reverse() // ['one', 'new item'] --> in place

## Dictionaries
my_dict = {'key1':'value1', 'key2':'value2'}
my_dict['key1'] // 'value1'
my_dict.keys() // dict_keys(['key1', 'key2'])
my_dict.values() // dict_values(['value1', 'value2'])
my_dict.items() // dict_items([('key1', 'value1'), ('key2', 'value2')]) --> returns tuples

## Tuples
* Tuples are immutable
* Tuples are faster than lists 
* Tuples use parentheses: (1,2,3)
t = ('a', 'a', 'c')
t.count('a') // 2
t.index('a') // 0
t.index('c') // 2

## Sets
* Sets are unordered collections of UNIQUE elements
* Sets do not have index
myset = set()
myset.add(1)
myset.add(2)
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist) // {1,2,3}

## I/O with Basic Files in Python
myfile = open('myfile.txt')
myfile.read() // 'Hello this is a text file\nthis is the second line\nthis is the third line'
myfile.seek(0) // 0 --> move the cursor to the beginning of the file because after you read the file, the cursor is at the end of the file
myfile.readlines() // ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line']
myfile.close()

The new way to open files is using the "with" statement, no longer need to close the file
with (open('myfile.txt')) as my_new_file:
    contents = my_new_file.read()

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()

* mode='r' is read only
* mode='w' is write only (will overwrite files or create new)
* mode='a' is append only (will add on to files),
* mode='r+' is reading and writing,
* mode='w+' is writing and reading (overwrites existing files or creates a new file)


## Comparison Operators & Logical Operators
and, or, not --> logical operators
1 < 2 adn 2 > 3 // False
not(1 == 1) // False
not 1 == 1 // False
not 400 > 5000 // True