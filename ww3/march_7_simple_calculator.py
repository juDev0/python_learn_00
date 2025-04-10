# SIMPLE CALCULATOR CALCULATION, ON TWO VARIABLE 
x = int(input ('what is the value for x:\n\r'))
y = int(input ('what is the value for y:\n\r'))

print(f'the addition of x and y value is: {x + y}')
print(f'the subtraction of x and y value is: {x - y}')
print(f'the multiplication of x and y value is: {x * y}')
print(f'the division of x and y value in one sf is: {x / y:.1f}')
print(f'the division of x and y value in two sf is: {x / y:.2f}')
print(f'the exponent of x and y value is: {x**y:.2f}')

# check if the values of x and y are either even or odd
if x % 2 == 0:
    print('x is a odd number')
else:
    print('x is an even number')

if y % 2 == 0:
    print('y is a odd number')
else:
    print('y is an even number')

print(f'the flour division of x and y value is: {x // y}')
