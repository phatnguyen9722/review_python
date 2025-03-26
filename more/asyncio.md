# Asyncio
- a Python library that is used for `concurrent programming`, including the use of `async iterator` in Python. </br>
- It is not `multi-threading` or `mutli-processing`. </br>
- `Asyncio` is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web servers, database connection libraries, distributed task queues, etc </br>

## Asynchronous Programming with Asyncio in Python
```python
import asyncio 

async def fn():
    print("This is")
    await asyncio.sleep(1)
    print("asynchronous programming")
    await asyncio.sleep(1)
    print("and not multi-threading")

asyncio.run(fn())
```

## Async Event Loop in Python
```python
import asyncio 

async def fn():
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print("four")
    await asyncio.sleep(1)
    print("five")

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())
```
- Now if you want the program to be actually asynchronous, In the actual order of execution we’ll need to make tasks in order to accomplish this. </be>
- This means that the other function will begin to run anytime if there is any free time using `asyncio.create_task(fn2())`. </br>

```python
import asyncio
async def fn():
    task=asyncio.create_task(fn2())
    print("one")
    #await asyncio.sleep(1)
    #await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    #await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
     
asyncio.run(fn())
```

```output
one
four
two
five
three
```

## I/O-bound tasks using asyncio.sleep()
- In this example, the `func1()`, `func2()`, and `func3()` functions are simulated I/O-bound tasks using asyncio.sleep(). They each “wait” for a different amount of time to simulate varying levels of work. </br>
- When you run this code, you’ll see that the tasks start concurrently, perform their work asynchronously, and then complete in parallel. The order of completion might vary depending on how the asyncio event loop schedules the tasks. This asynchronous behavior is fundamental to understanding how to manage tasks efficiently, especially when working with async iterators in Python. </br>

```python
import asyncio
 
 
async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")
 
 
async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")
 
 
async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")
 
 
async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended..")
 
 
asyncio.run(main())
```

## Difference Between Asynchronous and Multi-Threading Programming
- Asynchronous programming allows only one part of a program to run at a specific time. </br>
- Consider three functions in a Python program: `fn1()`, `fn2()`, and `fn3()`. </br>
- In asynchronous programming, if `fn1()` is not actively executing (e.g., it’s asleep, waiting, or has completed its task), it won’t block the entire program. </br>
- Instead, the program optimizes CPU time by allowing other functions (e.g., `fn2()`) to execute while `fn1()` is inactive. </br>
- Only when fn2() finishes or sleeps, the third function, fn3(), starts executing. </br>
- This concept of asynchronous programming ensures that one task is performed at a time, and other tasks can proceed independently. </br>
- In contrast, in multi-threading or multi-processing, all three functions run concurrently without waiting for each other to finish. </br>
- With asynchronous programming, specific functions are designated as asynchronous using the async keyword, and the asyncio Python library helps manage this asynchronous behavior. </br>