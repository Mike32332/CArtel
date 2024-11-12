import random
from random import randint 

miles = 15
cartel_miles = 0
food = 50
rest = 10
cartel_speed = random.randint(5, 15)  
cartel_speed2 = random.randint(10,30)
print("You have busted the cartel, escape to the US")

choice = input('What would you like to do? (click space)')

while miles < 300:
    choice = input("Enter '1' to travel, or '2' to scavenge, '3' to rest: ")

    if choice == '1':
        print('Would you like to travel by bike or by car?')
        choice = input("Enter 'b' to travel by bike, or 'c' travel by car: ")
        if choice == 'b':
            rnumber = random.randint(5, 20)
            miles += rnumber 
            print('You have traveled', rnumber, "miles")
            print('Total miles', miles)
            food -= 1
            rest -= 2
            cartel_miles += cartel_speed
            print("The Cartel is at", cartel_miles, "miles.")
            print('You have', rest, 'energy')
            print('You have', food, 'food')
        if choice == 'c':
            rnumber = random.randint(10, 30)
            miles += rnumber 
            print('You have traveled', rnumber, "miles")
            print('Total miles', miles)
            food -= 3
            rest -= 1
            cartel_miles += cartel_speed
            print("The Cartel is at", cartel_miles, "miles.")
            print('You have', rest, 'energy')
            print('You have', food, 'food')

    elif choice == '2':
        print('Would you like to look for food')
        choice =input("Enter 's' to scavenge")

        if choice == 's':
            rnumberf = random.randint(1,4)
            print('You have found', rnumberf, 'pounds of food')
            food += rnumberf 
            cartel_miles += cartel_speed
            print("The Cartel is at", cartel_miles, "miles.")
            print('You have', food, 'food')
            

    elif choice == '3':
        print('Would you like to rest for 1 or 2 days?')
        choice = input("How long?")
        if choice == '1':
            print('You have rested 1 day')
            food -= 1
            rest += 1
            cartel_speed = random.randint(5, 15)  
            print('You have', food, 'food')
            print('You have', rest, 'energy')
            print("The Cartel is at", cartel_miles, "miles.")

        if choice == '2':
            print('You have rested 2 days')
            food -= 2
            rest += 2
            cartel_miles += cartel_speed2
            print('You have', food, 'food')
            print('You have', rest, 'energy')
            print("The Cartel is at", cartel_miles, "miles.")

   

    if food < 1:
        print('You starved')
        quit()
    if rest <  1:
        print('You died by insomnia')
        quit()

    if cartel_miles >= miles: 
        print('The cartel caught you')
        quit()

    elif miles >= 300:
        print("Congratulations! You have reached the US")
