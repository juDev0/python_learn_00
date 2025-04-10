#CODE TO CHECK THE AGE OF A PERSON AND GRANT ASSES IF MEET REQUIREMENTS
#USING FUNCTIONS
def ageChecker(Age):
       if Age < 18:
            return('Asses denied youre not up to the requierd age\n\r')
       else:
            return('Asses granted! you can now procced.\n')

def start(ok) :
    if 'yes' in ok:
        age = int(input('Enter your age :\n\r'))
        print(ageChecker(age))

    else:
        return('alright have a great day!\n')
    
option = input('hello to create an acount we need to know your age proceed ? yes or no\n\r').strip().lower()
print(start(option))



#CODE TO CHECK THE AGE OF A PERSON AND GRANT ASSES IF MEET REQUIREMENTS
#WITHOUT USING FUNCTION
option = input('hello to create an acount we need to know your age proceed ? yes or no\n\r\t').strip().lower()
if 'yes' in option:
    age = int(input('enter your age: \n\r\t'))
    if age >= 18:
        print('Acces granted: you can now procced\n')
    else:
        print('Acces denied: sorry your Age didnt meet our requirements\n')
else:
    print('Ok! do have a great day.')
