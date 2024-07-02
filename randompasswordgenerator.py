import random

def random_password(user_input):
    
    if (user_input <8):
        print("Minimum range must be Eight!")
    else:
        password=""
        keys='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*-_+=<>?/'
        for i in range(user_input):
            password=password+random.choice(keys)
    print(password)


user_input=int(input('Enter the number:'))
random_password(user_input)

