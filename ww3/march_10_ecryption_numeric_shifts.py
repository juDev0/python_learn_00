#ENCRYOTION OF PASSWORD 

password = str(input(f'hello user kindly imput numeric password: \n\r\t').strip().upper())
for i in password:
    i = ord(i)
    i += password[i]
    print(i)
    #password = ord(password)
    #print('password denied input numbers only :')

   #newPassword = password << 2
   #print(newPassword)