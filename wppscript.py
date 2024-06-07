# by HelderJFLima

# This is a script that generates the parameters needed to use the
# 'wordsperpage' program.
#
# The user must inform the page numbers and number of lines requested during
# execution.


import random_numbers

psamplesize = 10   # Sample size of pages
lsamplesize = 4    # Sample size of lines

print('\n\n*** Parameters for the \'wordsperpage\' program ***\n')

firstpage = int(input('Enter the first page number: '))

lastpage = int(input('\nEnter the last page number: '))

print('\nRandom sample of pages:\n')

# Generate list of random values
random_numbers.generate(firstpage, lastpage, psamplesize)

for i in range(psamplesize):
    print('\n* Sample page #{} *\n'.format(i + 1))

    lnumber = int(input('Enter the number of lines: '))

    print('\nRandom sample of lines:\n')

    random_numbers.generate(1, lnumber, lsamplesize)

print('\n\nEnd of execution\n')
