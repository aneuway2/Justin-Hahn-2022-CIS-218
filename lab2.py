""" Justin Hahn
Lab 2
Egg dillema

Data collected: 
Peewee - less than 42 grams
Small - at least 42 grams
Medium - at least 49 grams
Large - at least 56 grams
Extra Large - at least 64 grams
Jumbo - 70 grams or more
from: https://www.getcracking.ca/recipes/article/making-substitutions-for-different-egg-sizes-and-weights """

while (True):
    weight = float( input ("Please type in the weight of the egg in grams"))

    # comment line experiment
    assert ( weight >= 0)    
    # Attempt 1

    if weight >= 70:
        egg = "jumbo"
    elif weight >= 64:
        egg = "extra large"
    elif weight >= 56:
        egg = "large"
    elif weight >= 49:
        egg = "medium"
    elif weight >= 42:
        egg = "small"
    else:
        egg = "peewee"

    print ("An egg weighing ",weight, " grams can be classified as ",egg)
