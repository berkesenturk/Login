import pymongo

class User():
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def login(self):
        self.username = username
        self.password = password
        
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        
        for i in mycol.find({},{ "_id": 0, "name": 1, "email": 1 }):
            if x == username:
                print("login successful")
        

        
        


    def register(self,email,pass_check):
        self.username = username
        self.password = password
         
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        d = {}
        if password == pass_check:
            d['name'] = username
            d['passwords'] = password
            d['email'] = email
            
            x = mycol.insert_one(d)
            print("You've registered successfully!")
        


        
            


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
