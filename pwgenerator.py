
import string
import random

if __name__ == "__main__":

    s1 = string.ascii_lowercase

    s2 = string.ascii_uppercase

    s3 = string.digits

    s4 = string.punctuation
    while True:
        try:
            passwordlen = int(input("Enter password length: \n")) 
            break
        except ValueError:
            print("It's not the valid number! Please try again")
    
    s = []
    s.extend(list(s1))  #list of s1  
    s.extend(list(s2))  #list of s2
    s.extend(list(s3))  #list of s3
    s.extend(list(s4))  #list of s4

    print("Your password is: ")
    print("".join(random.sample(s, passwordlen)))


