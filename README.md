# Julia for Python Programmers

## Comments

### Single-line comment

#### Python
```python
# Single-line comment in Python
```

#### Julia
```julia
# Single-line comment in Julia
```

### Multi-line comment

#### Python
```python
"""
Multi-line string
often used as a docstring
in Python
"""
```

#### Julia
```
#=
Here is a
multi-line comment
in Julia
=#
```

## Range

#### Python
```python
range(1, 11)  # range(1, 11)

type(range(1, 11))  # range

list(range(1, 11))  # [1, ..., 10]
```

#### Julia
```julia
1:10 # 1:10

typeof(1:10) # UnitRange{Int64}

collect(1:10) # 10-element Array{Int64,1}: 1, ..., 10
```

Notice that in Julia, both ends are inclusive.

## Functions

### vs Operators

#### Python
```python
# '+' is an operator in Python
1 + 2

# Using `operator` from standard library
import operator
operator.add.__doc__  # 'add(a, b) -- Same as a + b.'
operator.add(1, 2)
```

#### Julia
```julia
1 + 2

# Operators are just functions in Julia
+ # + (generic function with 171 methods)

# So, you can do this (where 1 and 2 are arguments to the function `+`)
+(1, 2)

# Or even this (like Lisp)
+(1, 2, 3, 4) # 10
```

### User-defined functions

#### Python
```python
def my_add(a, b):
    return a + b
```

#### Julia
```julia
function my_add(a, b)
    +(a, b)
end
```

In Julia, functions return the value of their last expression. `return` is only optional.

### Closure

#### Python
```python
def my_add_2(a):
    def nested(b):
        return a + b
    return nested

my_add_2(1)(2)
```

#### Julia
```julia
function my_add_2(a)
    function nested(b)
        +(a, b)
    end
end

my_add_2(1)(2)
```

### Anonymous functions

#### Python
```python
my_add_3 = lambda a, b: a + b
```

Python lambda is just a single expression.

#### Julia
```julia
my_add_3 = (a, b) -> +(a, b)
```

Julia anonymous function can take a multi-line body. See below.

```julia
my_add_4 = begin
    (a, b) ->
    +(a, b)
end
```

### With variable arguments

### With optional arguments

### With keyword arguments

### High-order function examples (Map/Filter/Reduce)

#### Python
```python
import functools
import operator

list(map(lambda x: x * 2, range(1, 6)))  # [2, 4, 6, 8, 10]

list(filter(lambda x: x % 2 == 0, range(1, 11)))  # [2, 4, 6, 8, 10]

functools.reduce(operator.add, range(1, 5))  # 10
```

Notice that `reduce` is no longer a built-in function in Python 3.x. Also, in Python 3.x, `map` and `filter` return `map` and `filter` objects respectively. They are lazily evaluated, however, they are strict in Julia. See below.

#### Julia
```julia
map(x -> x * 2, 1:5) # 5-element Array{Int64,1}: 2, ..., 10

filter(iseven, 1:10) # 5-element Array{Int64,1}: 2, ..., 10

reduce(+, 1:4) # 10
```

## Control flow

### If-Else

#### Python
```python
# if-elif-else
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# With ternary operator, `a if cond else b`
x if x >= 0 else -1
```

#### Julia
```julia
# if-elseif-else
if n > 0
    println("n is positive")
elseif n < 0
    println("n is negative")
else
    println("n is zero")
end

# With ternary operator, `cond ? a : b`
n > 0 ? n : -1
```

### for-loop

### while-loop

## Data Structures

### Tuple

### Vector (1-d array)

### Dictionary

### Set

## List/Array comprehension

### Without conditional

#### Python
```python
[x ** 2 for x in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

#### Julia
```julia
[x^2 for x in 1:10] # 10-element Array{Int64,1}: 1, ..., 100
```

### With conditional

#### Python
```python
[x ** 2 for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]
```

#### Julia
```julia
[x^2 for x in filter(iseven, 1:10)] # 5-element Array{Any,1}: 4, ..., 100
```

There is no conditional array comprehension in Julia, but you can use `filter` instead like shown above.

## Context management

### Example: Opening/closing file

#### Python
```python
with open("sample.txt") as f:
    for line in f:
        print("line: %s" % line)
```

#### Julia
```julia
open("sample.txt") do f
    for line in readlines(f)[1:5]
        println("line: $line")
    end
end
```

## Generator vs Task

#### Python
```python
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f = fib()  # <generator object fib at 0x10bf75728>
next(f)  # 1
next(f)  # 1
next(f)  # 2
next(f)  # 3
next(f)  # 5
next(f)  # 8
```

#### Julia
```julia
function fib()
    a, b = 0, 1
    while true
        produce(b)
        a, b = b, a + b
    end
end

f = Task(fib) # Task (runnable)
consume(f) # 1
consume(f) # 1
consume(f) # 2
consume(f) # 3
consume(f) # 5
consume(f) # 8
```

## Try-Catch

#### Python
```python
try:
    # Do something
except IndexError as e:
    # ...
except KeyError as e:
    # ...
except Exception as e:
    # ...
```

#### Julia
```julia
try
    # Do something
catch e
    if isa(e, BoundsError)
        # ...
    elseif isa(e, KeyError)
        # ...
    else
        # ...
    end
end
```
