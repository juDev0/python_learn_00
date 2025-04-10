#PROFILE GENERATOR for 3 workers WITH THE USE OF FUNCTION
print('hello! user, to create a profile of 3, fill in the details below\n')
def out1(m):
    m = [name1,age1,location1,contact1]
    print(f'PROFILE1:\n\r{name1}\n\r{age1}\n\r{location1}\n\r{contact1}\n\n')

def out2(m):
    m = [name2,age2,location2,contact2]
    print(f'PROFILE2:\n\r{name2}\n\r{age2}\n\r{location2}n\r{contact2}\n\n')

def out3(m):
    m = [name3,age3,location3,contact3]
    print(f'PROFILE3:\n\r{name3}\n\r{age3}\n\r{location3}\n\r{contact3}\n\n') 

name1 = str(input('\nEnter Name:\n\r\t')).strip().title()
age1 = str(input('Enter Age:\n\r\t'))
location1 = str(input('Enter Location:\n\r\t')).strip().title()
contact1 = input('Enter Phone Number or Email:\n\r\t')
a =[name1, age1, location1, contact1]

name2 = str(input('\nEnter Name:\n\r\t')).strip().title()
age2 = str(input('Enter Age:\n\r\t'))
location2 = str(input('Enter Location:\n\r\t')).strip().title()
contact2 = input('Enter Phone Number or Email:\n\r\t')
b =[name2,age2,location2,contact2]

name3 = str(input('\nEnter Name:\n\r\t')).strip().title()
age3 = str(input('Enter Age:\n\r\t'))
location3 = str(input('Enter Location:\n\r\t')).strip().title()
contact3 = input('Enter Phone Number or Email:\n\r\t')
c =[name3,age3,location3,contact3]

out1(a)
out2(b)
out3(c)


#CREATES AND PRINTS A PROFILE WITHOUT THE USE OF FUNCTION
name = str(input('Enter Name:\n\r\t')).strip().title()
age = str(input('Enter Age:\n\r\t'))
location = str(input('Enter Location:\n\r\t')).strip().title()
contact = input('Enter Phone Number or Email:\n\r\t')
m = [name, age, location, contact]
profile2 = print(f'PROFILE:\n\r{name}\n\r{age}\n\r{location}\n\r{contact}\n\n')