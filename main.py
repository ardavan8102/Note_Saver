# Don't Change These!
while True:
    print('Welcome My Dear User !')
    print('You Are Using Note Saver Alpha Version!')
    print('Enter password To See Passwords ')
    print('Enter notes To See Notes')
    print('Enter users To See Usernames')
    user_input = input(">> Write Here : ")
    # Closing Program
    if user_input == "quit":
        print("exit")
        break
    # Your Passwords
    elif user_input == "password":
        print(">> Your Saved Passwords : \n >> Instagram : 1234 \n >> Steam : 1234")  
    # Your Notes
    elif user_input == "notes":
        print(">> Your Saved Notes : \n >> 12th Of Agust I Have math Exam! \n >> I have To Buy Gift For My Mom 15th September This Year")
    # Your Users
    elif user_input == "users":
        print(">> Your Saved Usernames : \n >> Instagram : Ardavan81 \n >> Telegram : Ardavan8102")
    
    else:
        print("Unknown Command")      