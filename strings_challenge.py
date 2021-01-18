def username_checker():
    username = input("Enter your username: ")
    user = ""

    while True:
        if len(username) < 6 or username.find('_') == -1:
            username = input("Please enter your Valid username: ")
        else:
            break

    if username[-1:] == 'S':
        user = "Student"
        print(f"The user is a {user}")
        if username[0:1] == "0":
            print(f"The year group of the student is {username[1:2]}")
        else:
             print(f"The year group of the student is {username[0:2]}")
        #print(f"The student's name is {username[2:3]} {username[3:-2]}")
        print("The user " + username[2:3].upper() + " "+ username[3:-2] + " is an " + user)
    elif username[-1:] == 'T':
        user = "Teacher"
        #print(f"The user" + username[2:3].upper() + " {username[3:-2]} is a {user}")
        print("The user " + username[2:3].upper() + " "+ username[3:-2] + " is an " + user)

    elif username[-1:] == 'A':
        user = "Admin staff"
        print("The user " + username[2:3].upper() + " "+ username[3:-2] + " is an " + user)
    else:
        print("Not a valid username")
        exit()

    
username_checker()