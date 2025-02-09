# by HelderJFLima

# functions used by wppscript.


import cmath as cm
import os
from typing import Union


def confirm_value(value: Union[int, float]) -> bool:
    """

    Ask the user to confirm a given value.

    :param value: value to be confirmed by the user.

    :return: True or False, if the user's answer is 'y' or 'n'.

    """

    answer = ''

    print(f'\nDo you confirm the value {value}?')

    while answer != 'y' and answer != 'n':
        answer = input('\nAnswer (y/n): ').lower()

    return answer == 'y'


def get_float() -> float:
    """

    Get a valid float value and prompt the user to confirm or correct it.

    :return: the value informed by the user.

    """

    unchecked = True
    number = 0.0

    # Get a valid value and confirm it
    while unchecked:
        try:
            number = abs(float(input()))

        except (ValueError, TypeError):
            print('\nInvalid value!\n\nPlease enter a positive number: ',
                  end='')
            continue

        except OverflowError:
            print('\nInvalid value!\n\nPlease enter a smaller value: ',
                  end='')
            continue

        # In case of zero, 'nan' or 'inf'
        if number == 0.0 or cm.isnan(number) or cm.isinf(number):
            print('\nInvalid value!\n\nPlease enter a valid number: ',
                  end='')
            continue

        if confirm_value(number):
            unchecked = False
        else:
            print('\nEnter a new value: ', end='')

    return number


def get_integer() -> int:
    """

    Get a valid integer value and prompt the user to confirm or correct it.

    :return: the value informed by the user.

    """

    unchecked = True
    number = 0

    # Get a valid value and confirm it
    while unchecked:
        try:
            number = abs(int(input()))

        except (ValueError, TypeError):
            print('\nInvalid value!\n\nPlease enter a positive number: ',
                  end='')
            continue

        # In case of zero
        if number == 0:
            print('\nInvalid value!\n\nPlease enter a valid number: ',
                  end='')
            continue

        if confirm_value(number):
            unchecked = False
        else:
            print('\nEnter a new value: ', end='')

    return number


def save_values(file_name: str, values: tuple) -> None:
    """

    Save the results to a file and inform the user of the directory.

    :param file_name: output file name.

    :param values: tuple with the lists of values.

    :return: None

    """

    # Write the strings to the file
    with open(file_name, mode='w') as f:
        for i in range(2):
            f.write(string_from(values[i]))

        for i in range(len(values[2])):
            f.write(string_from(values[2][i]))

    print('\nThe output was saved in:\n')

    # Display the path
    print(os.getcwd() + '\\' + file_name + '\n')


def string_from(lst: list) -> str:
    """

    Get a string consisting of comma-separated values from a list and append
    a newline at the end.

    :param lst: list with values.

    :return: a string composed of the values.

    """

    # remove brackets and whitespace
    s = str(lst).strip('[]').replace(' ', '')

    return s + '\n'
