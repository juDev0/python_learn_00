#building calculator

#FIRST INT DATATYPE
x = input("what's x? ").strip()
y = input("what's y? ").strip()

print(int(x) + int(y))

'''one is a way to solve it
the other, is another way to solve it'''

a = int(5)
b = int(5)
print(a + b)

'''one is a way to solve it
the other, is another way to solve it'''

i = int(input("what's i? ").strip())
j = int(input("what's j? ").strip())

print(i + j)

#FLOT DATATYPE
any_1 = input("enter any number").strip()
any_2 = input("enter sec numbrer").strip()
z = float(any_1)/float(any_2) 
m = float(any_1)/float(any_2)
m = round(m,2)

#rounds up z by formating to 2fig
print(f"{z:.2f}")

#rounds up z by the use of the round fnc
print(m)