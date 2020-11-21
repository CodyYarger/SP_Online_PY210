#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/21/2020 - csimmons

# list data for all exercises
fruits = ['Apples', 'Pears', 'Oranges', 'Blueberries']

def series_one(fruits):
    # Display the list of fruits
    print('We have the following fruits available: ' + str(fruits))
    # Ask user for another fruit and add to end of the list
    add_fruit = input('What kind of fruit do you want to add?  ')
    fruits.append(add_fruit)
    # Display the list of fruits again
    print('The following fruits are now available: ' + str(fruits))
    # Ask user to select one of the fruits in above list by position
    print('Select one of the above fruits by its position in the list')
    fruit_idx = input('Please enter a number: ')
    print(fruits[(int(fruit_idx)-1)] + ' are in position ' + str(fruit_idx))
    # add additional fruit to list via concatenation and insert()
    fruits = ['Pineapples'] + fruits
    print(str(fruits) + ' Pineapples added to list')
    fruits.insert(0, 'Bananas')
    print(str(fruits) + ' Bananas added to list')
    #Display all fruits that begin with 'P' using for loop
    for fruit in fruits:
        if fruit.startswith("P"):
            print(fruit)
    return fruits


def series_two(fruits):
    #using the list from series_one, display it
    print(fruits)
    #Remove last fruit from list and display
    fruits.pop(-1)
    print(fruits)
    #Ask user for fruit to delete. Find the fruit and delete
    user_remove = input("Please select a fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in fruits:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    else:
        fruits.remove(user_remove)
    print(fruits)
    # Bonus Section - Multiply list times two. Keep asking until match is found
    # Once found, delete all occurences
    double_fruit = fruits * 2 
    print(double_fruit)
    user_remove = input("Please select another fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in double_fruit:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    for fruit in double_fruit:
        while user_remove in double_fruit:
            double_fruit.remove(user_remove)
    print(double_fruit)
    return(double_fruit)


series_one(fruits)
series_two(fruits)