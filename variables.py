## if statements
"""
if condition:
    logic
elif condition:
    logic
else:
    log
    """
     
    ##  A programme that accepts a number from the user(1-9)
    # it tells him the number entered
    
       
print("welcome to number teller!")
number = int(input("please enter a number between 1 and 9"))
if number == 1:
    print("ÿou have entered number one")
elif number == 2:
    print("you have entered number two")
elif number == 3:
    print("you have entered number three")
elif number == 4:
    print("you have entered number four") 
elif number == 5:
    print("you have entered number five")        
else:
    print("invalid, please enter a number between 1 and 9") 
    
    
    #TODO
    '''
    with use of if statements, write a python program that allows an instructor to enter a mark strictly between 0 and 100.
    on receiving the mark, he program has to assign a grade based on your define clusters ie 80-90 is A etc.
    '''
        