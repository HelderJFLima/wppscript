# by HelderJFLima

# This is a script that generates the parameters needed to use the
# 'wordsperpage' program.
#
# The user must inform the page numbers, numbers of lines and numbers of words
# requested during execution.


import random
from wppscript_functions import *


page_sample_size = 10          # Sample size of pages
lines_sample_size = 4          # Sample size of lines

output_file_name = "wpp_input.txt"

print('\n\n*** Parameters for the \'wordsperpage\' program ***\n')

start_finish_pages = []

print('\nEnter the initial page number: ', end='')

start_finish_pages.append(get_integer())             # Initial page

print('\nEnter the final page number: ', end='')

start_finish_pages.append(get_integer())             # Final page

rng_limit = tuple(start_finish_pages)   # Limits for the random number generator

numbers_of_lines = []

numbers_of_words = []

random.seed()                           # Initialize the random number generator

for i in range(page_sample_size):
    rnd_number = random.randint(rng_limit[0], rng_limit[1])

    print(f'\n*Page {i + 1} of {page_sample_size}:  {rnd_number}')

    print('\nEnter the number of lines: ', end='')

    numbers_of_lines.append(get_integer())           # Get number of lines

    nlines = numbers_of_lines[-1]      # Upper bound for random number generator

    wnumbers = []                      # To store number of words

    for j in range(lines_sample_size):
        rnd_number = random.randint(1, nlines)

        print(f'\n**Line {j + 1} of {lines_sample_size}:  {rnd_number}')

        print('\n  Enter the number of words: ', end='')

        wnumbers.append(get_float())                 # Get number of words

    numbers_of_words.append(wnumbers)

data = tuple([start_finish_pages, numbers_of_lines, numbers_of_words])

save_values(output_file_name, data)                  # Save file with data
