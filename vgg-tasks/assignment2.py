import math
print("................QUESTION 1......................")
#this count function will the count number of upper and lower case letters of any string passed into it.
def count(*args):
    count_lower = 0
    count_upper = 0
    for arg in args:
        print(arg)
        for items in arg:
            lower = items.islower()
            upper = items.isupper()
            if (upper):
                count_upper = count_upper + 1
            elif (lower):
                count_lower = count_lower + 1

    print("No. of Upper case: ", count_upper)
    print("No. of Lower case: ", count_lower)

count("The quick Brow Fox")

#function to find the maximum of three numbers
print("................QUESTION 2......................")
def maximum_value(*args):
        maximum_value = max(args) 
        print("The maximum of this ist of numberd is : ", maximum_value)

maximum_value(20, 50, 40)

print("................QUESTION 3......................") 
def prime_number(x):
    if (x >= 2):

        for i in range(2, x):
            if (x % i) == 0:
                print (x," is not a prime number")
                break
        else:
            print(x," is a prime number")
    else:
        print(x," is not a prime number ")
prime_number(100)

