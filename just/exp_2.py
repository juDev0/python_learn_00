''' defining a functions'''

#normal function with one parameter
def main(proname):
    print(f"my God {proname} nice to meet you \n" * 2)

#function with 2 parameter
def calc(b,h):
    a = round((1/2)*int(b)*int(h))
    print("your answer is",a,"Enjoy \n")
    print(f"your answer is {((1/2)*int(b)*int(h)):,.2f} Enjoy \n")

#fionction with no lenght of parameter
def call(*num):
    print("the number is ringing",num[2])

#default parameter vAalue function in this you print the default value of the function
def country(cn="Nigeria"):
    print(f"{name} is from {cn}")

#return function
def pronum(x):
    return(x * 2)

#for getting in the name and printing it out
name = input("what is your name? \n").strip().title()
main(name)

#for calculating area
lenght = input("what lenght? ").strip()
height = input("what height? ").strip()
calc(lenght,height)

#for printig out a number
call(1,2,3,4,5,6)

#for printing the deafault country
person_1 = input("what country are you from? ").strip()
person_2 = input("what country are you from? ").strip()
country(person_1)
country(person_2)
country()

#for testing the return fnc
pronum(lenght)