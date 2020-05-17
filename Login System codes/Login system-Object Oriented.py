
class User():
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def login(self):
        self.username = username
        self.password = password
        

        
        with open("register.txt","r",encoding="utf-8") as file:
            if username == username and password == password:
                print("login successful!")


    def register(self,email,pass_check):
        self.username = username
        self.password = password
         
        
        if password == pass_check:
            print("Password matches, now you can login")
            with open("register.txt","a",encoding="utf-8") as file:
                file.write('Username: '+username+' \nPassword: '+password+' \nemail: '+email)
        else:
            print("passwork doesn't matches")
            


choice = int(input("1-Login  2-Register: "))

if choice == 1:     
    username = input("Enter username: ")
    password= input("Enter password: ")
    user = User(username,password)
    user.login()
elif choice ==2:
    username = input("Enter username: ")
    password= input("Enter password: ")
    pass_check= input("Enter password: ")
    email= input("Enter email: ")
    user = User(username,password)
    user.register(email,pass_check)


    
