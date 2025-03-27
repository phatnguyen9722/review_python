list_fruits = ["apple", "cherry", "orange", "strawberry", "peach", "pine apple"]

# Show List fruits
print("\n[STEP]: Show Original List fruits")
print("-----")
print(list_fruits)

# Access List items
print("\n[STEP]: Access List items")
print("-----")
print(list_fruits[0])
print(list_fruits[1])
print(list_fruits[-1])  # Last one
print(list_fruits[1:3])  # Index: 1, 2
print(list_fruits[1:])  # Index: 1 to last
print(list_fruits[-3:-1])  # Index: -3, -2

# Check if item is present to list
print("\n[STEP]: Check if item is present to list")
print("-----")
if "apple" in list_fruits:
    print("I have an apple")
else:
    print("Nope!")

# Change items
print("\n[STEP]: Change item/items")
print("-----")
list_fruits[1] = "lemon"  # Change cherry by lemon
print(list_fruits)

list_fruits[1:3] = ["kiwi", "mango"]
print(list_fruits)

# Insert items
print("\n[STEP]: Insert watermelon to index 1")
print("-----")
list_fruits.insert(1, "watermelon")
print(list_fruits)

# If we have list of colors like this:
colors = ["green", "red", "yellow", "green", "green", "red", "yellow"]

# Bad way
print("-------")
print("Bad way to concentrate 2 lists")
print("-------")
print(colors[0], list_fruits[0] + "\n" + colors[1], list_fruits[1])

# Good way
# Install pandas
print("-------")
print("Good way to concentrate 2 lists")
print("-------")
import pandas as pd

df = pd.DataFrame(columns=["COLOR", "FRUIT"])
df["COLOR"], df["FRUIT"] = colors, list_fruits

print(df)
