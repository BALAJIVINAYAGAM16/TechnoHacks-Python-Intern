import string
import random

def generate_random_pwd(n):

    lower   = string.ascii_lowercase
    upper   = string.ascii_uppercase
    num     = string.digits
    symbols = string.punctuation
    
    combinations = lower + upper + num + symbols

    temp = list(combinations)
    random.shuffle(temp)

    random_pwd = []

    i=0
    while i<n:
        random_pwd.extend(random.choice(temp))
        i+=1

    random.shuffle(random_pwd)
    password = ''.join(random_pwd)
    print("Password: "+password)


print("          Welcome to Random Password Generator!!!         ")

def main():
        length = int(input("Enter desired length of password: "))
        generate_random_pwd(length)
        re_pwd=int(input("Do you want to generate another password?\nif yes press 1, otherwise 0: "))
        if (re_pwd == 1):
            return main()
        else:
            quit()
       
main()
