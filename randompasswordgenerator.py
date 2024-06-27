import random
n=int(input('Enter the number'))
passs=''


a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*-_+=<>?/'
for i in range(n):
    passs=passs+random.choice(a)
    print(passs)
    
