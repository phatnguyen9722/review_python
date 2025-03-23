# Python enumerate

- Take a `collection` than return it as an enumerate object. </br>

## Definition and Usage
- The enumerate() function takes a `collection` (e.g. a tuple) and returns it as an `enumerate object`. </br>
- The enumerate() function adds a `counter` as the key of the `enumerate object`. </br>

## Syntax
```python
enumerate(iterable, start)
```

### Example: 
```python
x = ['apple', 'banana', 'cherry']
y = enumerate(x)

print(y)

for i, k in enumerate(x):
	print(i, k)
```

### Output:
```bash
<enumerate object at 0x14712b01e300>

0 apple
1 banana
2 cherry
```