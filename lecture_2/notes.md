# Lecture 2

## Overview

Developing programs in Python.

### Functions in Python

* `print()` prints the arguments to the screen.

* `input("Prompt:")`is used to get input from the user. No matter what you type, this function will return a string. So, you must cast the return value to whatever type you need it to be.

* `if-elif-else` is equivalent to if, else if, and else in other languages like Java and C.

* `int()` takes anything and turns it into an integer.

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