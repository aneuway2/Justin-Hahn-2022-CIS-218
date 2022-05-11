""" Justin Hahn
Lab 4: Dictionaries
"""


my_dict = {}
my_dict = {
    "soccer" : "A sport played with a round ball at your feet",
    "baseball" : "A sport played on a diamond with a bat and a ball",
    "ice hockey" : "A sport played on an ice rink with a puck and a stick"
    }

while True:
    y = 0
    x = input("Enter any word")
    if x in my_dict:
        print (my_dict[x])
    if x not in my_dict:
        y = input("That is not in this dictionary, Would you like to add it?")
        if y == "yes":
            print("Enter a definition: ")
            definition = input ()
            print (x, ":" , definition)
            my_dict[x] = definition
        elif y == "no":
            print("Try again")
