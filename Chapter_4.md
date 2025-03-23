# Python Zip 

## Definition and Usage
- The `zip()` function returns a `zip object`, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc. </br>
- If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator. </br>

## Syntax
```python
zip(iterator1, iterator2, iterator3,...)
```

### Example: 
```python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

print(x)
```
### Output
```bash
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
```
