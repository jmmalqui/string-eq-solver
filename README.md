# Mathematical Expression Evaluator

Receives a string and evaluates it as a mathematical expression

## Usage 

Download the zip file and paste it on your project, no extra dependecies required.

Basic operators such as:

```txt
"+" addtion
"-" substraction
"*" product
"/" division
"^" power
"%" modulo
```

can be used.

```python
my_equation = "2 + 3 * (4 ^ (3 - 1))"
solve_eq(my_equation)  # 50 
```

Variables can be passed by using fstrings.

```python 
time = 0
velocity = 10
distance = f"{time} * {velocity}"
solve_eq(distance) # 0 
for i in range(10):
    time += 1
    distance = f"{time} * {velocity}"
    solve_eq(distance) # 10 20 30 ... 
```
