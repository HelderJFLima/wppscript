# by HelderJFLima

# function used by wppscript.


import random


def generate(lower, upper, quantity):

    # Initialize the random number generator
    random.seed()

    for i in range(quantity):
        print(random.randint(lower, upper))
