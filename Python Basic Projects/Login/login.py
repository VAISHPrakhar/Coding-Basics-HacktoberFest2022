dict = {'shiv': 'shiv1234', 'raj': 'raj1234', 'rohan': 'rohan1234'}

username = input("enter your username: ")

if username in dict:
    password = input("Please enter you password: ")

    if dict[username]==password:
        print("You have successfully logged in !!")
    
    else:
        print("Invalid passeword !!")

else:
    print("You are not a valid user !!")
