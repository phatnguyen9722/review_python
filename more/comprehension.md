[👈 Back to main index](README.md)
# List Comprehension
- `List comprehension` offers a shorter syntax when you want to create a new list based on the values of an existing list. </br>

###### Example:
- Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name. </br>
- Without `list comprehension` you will have to write a for statement with a conditional test inside: </br>

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```
- With list comprehension you can do all that with only one line of code: </br>

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```