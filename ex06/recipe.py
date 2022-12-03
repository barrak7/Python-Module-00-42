#!/bin/python
import sys

cookbook = {'Sandwich':{'ingredients':'ham, bread, cheese, tomatoes', 'meal':'lunch', 'prep_time':10}, 'Cake':{'ingredients':'flour, sugar, eggs', 'meal':'dessert', 'prep_time':60}, 'Salad':{'ingredients':'avocado, arugula, tomatoes, spinach', 'meal':'lunch', 'prep_time':15}}

def pr(i, name=None):
    if name == None:
        print("\n")
        for key in cookbook.keys():
            print(key)
        print("\n")
    elif name not in cookbook.keys():
        print("\nSorry, this meal is not in the cookbook.\n")
    else:
        if (i == 3):
            print("\nRecipe for", name)
            print("\tIngredients list:", cookbook[name]['ingredients'].split(", "))
            print("\tTo be eaten for", cookbook[name]['meal'])
            print("\tTakes {}mins to prepare.\n".format(cookbook[name]['prep_time']))
        else:
            print("\nRecipe deleted successfuly!\n")
            cookbook.pop(name)

def radd():
    rec = input("\nEnter a name: ")
    cookbook[rec] = {}
    i = 0
    j = ""
    while i != "":
        i = input("Enter ingredients: ")
        j = ' '.join([i, j])
    j = j.strip()
    j = j.replace(" ", ", ")
    cookbook[rec]['ingredients'] = j
    cookbook[rec]['meal'] = input("Enter a meal type: ")
    cookbook[rec]['prep_time'] = input("Enter a preparation time: ")
print("Welcome to the Python Cookbook !")
def fun():
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")

    name = None
    choice = input("\n\nPlease select an option:\n>> ")
    if (choice.isnumeric() == 0 or int(choice) not in range(1, 6)):
        print("Sorry, this option does not exist.")
    else:
        if(int(choice) == 1):
            radd()
            print("\n")
        elif (int(choice) == 2):
            name = input("\nPlease enter the name of the recipe to be deleted:\n>> ")
            pr(2, name)
        elif (int(choice) == 3):
            name = input("\nPlease enter the name of the recipe to be printed:\n>> ")
            pr(3, name)
        elif (int(choice) == 4):
            pr(4, name)
        else:
            print("\nCookbook closed, goodbye!")
            sys.exit()
    fun()
fun()
