[👈 Back to main index](README.md)
# Chapter 1:
## Index
- [1. Basic syntax](#1-basic-syntax) </br>
- [2. Data Types](#2-data-types) </br>
- [3. Conditionals](#3-conditionals) </br>
- [4. loop](#4-loop) </br>
    - [`While` loop](#while-loop) </br>
    - [`For` loop](#for-loop) </br>
- [5. Type casting](#5-type-casting) </br>
- [6. Python Collections](#6-python-collections-arrays) </br>
- [7. Exceptions](#7-exceptions) </br>
- [8. Functions | Builtin Functions](#8-functions--builtin-functions) </br>

### 1. Basic syntax
-----
#### Python Indentation
- `Indentation` refers to the spaces at the beginning of a code line. </br>
- Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. </br>
- Python uses indentation to indicate a block of code. </br>

#### Python Variables
- In Python, variables are created when you assign a value to it </br>
- Variable names are `case-sensitive` (A != a). </br>

### 2. Data Types
-----

### 3. Conditionals
-----

### 4. loop
-----
#### While loop
```python
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello World!")
```
#### For loop
```python
n = 4
for i in range(0, n):
    print(i)
```

### 5. Type Casting
-----
#### Specify a Variable Type
- There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types. </br>
- Casting in python is therefore done using constructor functions: </br>
    - `int()` - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    - `float()` - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    - `str()` - constructs a string from a wide variety of data types, including strings, integer literals and float literals

### 6. Python Collections (Arrays)
-----
- There are four `collection data types` in the Python programming language: </br>
    - `List` is a collection which is ordered and changeable. Allows duplicate members. </br> 
    - `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members. </br> 
    - `Set` is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. </br> 
    - `Dictionary` is a collection which is ordered** and changeable. No duplicate members. </br> 

### 7. Exceptions
-----
#### Try --- except 
- The `try` block lets you test a block of code for errors. </br> 
- The `except` block lets you handle the error. </br> 
- The `else` block lets you execute code when there is no error. </br> 
- The `finally` block lets you execute code, regardless of the result of the try- and except blocks. </br> 

```python
x = 5

try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("Done")
```

#### Raise an exception
- As a Python developer you can choose to throw an exception if a condition occurs. </br> 
- To throw (or raise) an exception, use the `raise` keyword. </br> 
- The `raise` keyword is used to raise an exception. </br> 
- You can define what kind of error to raise, and the text to print to the user. </br> 

```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```

### 8. Functions | Builtin Functions
-----