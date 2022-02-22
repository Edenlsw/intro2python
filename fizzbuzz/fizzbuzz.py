

# this is basic fizzbuzz code. 
# -----------------------------------
# def challenge(num):

#   if num % 15 == 0:
#     return "FizzBuzz"
#   elif num % 5 == 0:
#     return "Buzz"
#   else:
#     return "Fizz"

# challenge(15)
# -----------------------------------

# def challenge(num):

#   if num % 3 == 0 and num % 5 == 0:
#     return "FizzBuzz"
#   elif num % 5 == 0:
#     return "Buzz"
#   elif num % 3 == 0:
#     return "Fizz"
#   else:
#     return num

# -----------------------------------






  




# ------------------------------------------------



# def challenge(i):
#   for i in range(1, 101):
#       if i % 15 == 0:
#           print("FizzBuzz")
#       elif i % 3 == 0:
#           print("Fizz")
#       elif i % 5 == 0:
#           print("Buzz")
#       else:
#           print(i)

# challenge(100)



def challenge(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i


def main():
    for i in range(1, 101):
        print(challenge(i))


if __name__ == '__main__':
    main()