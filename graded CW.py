import random
def main():
    # ex1()
    # ex2()
    # ex3()
    ex4()


# Create a random number. Print the number.
def ex1():
    randomNum = random.randint(0,1000)
    print(randomNum)

# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def ex2():

    secret = "code"

    while (True):
        ask = input("enter password. q to quit")
        if ask == secret:
            print("Access Granted")
            break
        elif ask == "q":
            break

# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.
def ex3():
    while (True):
        ask = int(input("enter a positive integer. '0' to quit"))
        for i in range(0,ask+1):
            print(i)
        if ask == 0:
            break


# Create a function that creates a random number.
# Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.
def ex4():
    randomNumber = random.randint(0,100)
    
    while(True):
       
        ask = int(input("guess the random number from 0 to 100"))
        
        if ask == randomNumber:
            break
        elif ask > randomNumber:
            print("lower")
        elif ask < randomNumber:
            print("higher")
    

            
        



if __name__ == '__main__':
    main()