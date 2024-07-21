# Lecture 2

## Overview

Developing programs in Python.

### Functions in Python

* `print()` prints the arguments to the screen.

* `input("Prompt:")`is used to get input from the user. No matter what you type, this function will return a string. So, you must cast the return value to whatever type you need it to be.

* `if-elif-else` is equivalent to if, else if, and else in other languages like Java and C.

* `int()` takes anything and turns it into an integer.

* To define your own function, use def. For example:
```
def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

### Terminologies and things to know

* Python is an **interpreted language**, meaning if you run a program called python, which is an **interpreter**, it will read your py file line by line, executing each line and interpreting what it is that it means in a way that the computer can understand.

* To run a py file, type in your terminal `python <filename.py>`

* Python doesn't require you to explicitly state what the type of each variable is.

* Boolean values can be represented using True with a capital T or False with a capital F.

* NoneType: A special type in python which has only one possible value, a capital N, None. It is used to represent the lack of a value somewhere. If a function is not returning anything, it is returning None effectively.

* '+' operater will add 2 numbers or concatenate 2 strings.

* fstrings are formatted strings. put an f before quotation marks. For example: 
```
name = input("Name:")
print(f"Hello, {name}!")
```

* **Indentation** is required because the indentation is how the program knows what code is inside of the if statement and what code is outside of the if statement. 

* **Sequences** in Python are data types that store values in some sort of sequence or some collection of values altogether. Multiple elements can have the same value.

* Mutable means you can change the elements, i.e., add new elements, remove elements, and change the values of elements.

* Immutable mean you cannot change the elements.

* Types of Sequences:

    1. **String**. Can access different characters within the string using `string[i]` where string is the string whose character you want to extract and i is the index of the required character. Methods:
        - `len(string)`gives the number of characters in a string.
    2. **List**: Can store any type of data inside a list in Python. It is a sequence of mutable values.
    3. **Tuple**: A tuple is used when you have a couple of values that are not going to change but you need to store 2 or more values together. Sequence of immutable values.

* Types of Data Structures:

    1. **List**: Methods:
        - `.append(i)` to add a new element 'i' to the end of the list.
        - `.sort()` to sort the elements in a particular order. The order is not user defined.
        - `len(list)` gives the number of elements inside a list.
    2. **Tuple**
    3. **Set**: collection of unique values. Does not keep things in a particular order. Methods:
        - `.add(i)` to add a new element 'i', not in a particular order.
        - `.remove(i)` to remove a particular element 'i' from anywhere in the set.
        - `len(set)` gives the number of elements inside a set.
    4. **dict**: collection of key-value pairs.
    ```
    # define a dictionary
    ages = {"Alice": 22, "Bob": 27}

    # accessing a particular value using a key
    print(ages["Alice"])

    # to add a new key-value pair to a dict
    ages["Charlie"] = 30
    ```

### Loops in Python

* For Loop:
    ```
    for i in [0, 1, 2, 3, 4]:
        print(i)
    
    # is equivalent to 
    
    for i in range(5):
        print(i)
    ```
* For each loop
    ```
    for element in list:
        print(element)
    
    # or

    for character in string:
        print(character)
    ```
