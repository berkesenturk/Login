
choice = int(input("1-Login  2-Register"))

if choice == 1:
    username = input("Enter username: ")
    password= input("Enter password: ")
    with open("register.txt","r",encoding= "utf-8") as file:        
        if username == username and password == password:
            print("LOGIN SUCCESFUL!")
        
elif choice == 2:
    username = input("Enter username: ")
    password= input("Enter password: ")
    pass_check= input("Enter password: ")
    email= input("Enter email: ")

    if password == pass_check:
        print("Password matches, you can login")
        with open("register.txt","a",encoding="utf-8") as file:
            file.write('Username:'+username+' \nPassword:'+password+' \nemail:\n'+email)
        
else:
    pass
   





















