#!/usr/bin/env python3

## 1 ############################################################################################################
# Exercise - Guess the Number:
# - Generate a random integer from 1 to 100.
# - Ask the user repeatedly to guess the number.
# - Until they guess correctly, tell them to guess higher or lower.

import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')


## 1.1 ############################################################################################################
# Exercise - Guess the Number with 3 Chances:
# - Generate a random integer from 1 to 100.
# - Ask the user repeatedly to guess the number.
# - Give them 3 chances to guess correctly, tell them to guess higher or lower.

import random

def guessing_game():
    
    answer = random.randint(0, 100)
    remaining_guesses = 2

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

    else:
        print('Your three chances are up!')


## 1.3 ############################################################################################################
# Exercise #1.3 - Guess the word:
# - Choose a random word from the nltk words list.
# - Ask the user repeatedly to guess a word.
# - Until they guess correctly, tell them to guess one that's earlier or later in the dictionary based on alphabetical order.

import random
import nltk

# Download the words corpus if it hasn't been downloaded yet
nltk.download('words')

# Load English words from nltk
from nltk.corpus import words
WORDS = words.words()

def guessing_game():

    answer = random.choice(WORDS).lower()  # Ensure the word is in lowercase for comparison

    print("Guess the word! I'm thinking of an English word.")
    while True:
        user_guess = input('What is your guess? ').lower()  # Convert guess to lowercase

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        # Since we're dealing with strings, we compare their lexicographical order
        if user_guess < answer:
            print(f'Your guess of {user_guess} comes alphabetically before the answer.')

        else:
            print(f'Your guess of {user_guess} comes alphabetically after the answer.')

if __name__ == "__main__":
    guessing_game()


## 2 ############################################################################################################
# Exercise - Create a function to calculate sum
# - Create a function that accepts any number of numeric arguments as inputs.
# - Return the summ of those numbers.
# - If invoked without any arguments, returns 0.

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


## 2.1 ############################################################################################################
# Exercise - Create a function to calculate sum and include the option of a starting number
# - Create a function that accepts any number of numeric arguments as inputs.
# - Return the summ of those numbers.
# - Mimic the built-in sum function by adding the capacity to provide a starting value as the second argument.
# - If invoked without any arguments, returns 0.

def mysum(numbers, start=0):
    output = start
    for number in numbers:
        output += number
    return output


## 2.2 ############################################################################################################
# Exercise - Calculate mean from a non-empty list of numbers

def mean(numbers):
    return mysum(numbers) / len(numbers)

## 2.3 ############################################################################################################
# Exercise - Calculate mean number of characters from a list of words
# - Write a function that takes a list of words (strings). 
# - It should return a tuple containing three integers, representing the length of: (1) the shortest word, (2) the length of the longest word, (3) and the average word length.

def summarize(words):
    word_lengths = [len(one_word)
                    for one_word in words]

    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)

## 2.4 ############################################################################################################
# Excercise - Calculate the sum while ignoring non viable inputs
# - Write a function that takes a list of Python objects. 
# - Sum the objects that either are integers or can be turned into integers, ignoring the others.

def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False


def sum_intable(items):
    return sum(one_item
               for one_item in items
               if is_intable(one_item))

## 3 ############################################################################################################
# Exercise - Create a log of 10km run time for user
# - Write a function (run_timing) that asks how long (in minutes) it took the user to run 10 km.
# - Continue to ask for data on addtional runs until the user presses Enter. 
# - Thenn calculating and displaying the average time that the 10 km runs took.

def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    if number_of_runs > 0:
        average_time = total_time / number_of_runs
        print(f'Average of {average_time}, over {number_of_runs} runs')
    else:
        print('No runs entered.')

run_timing()

## 3.1 ############################################################################################################
# Exercise - Truncate digits before and after the decimal point
# - Write a function that takes 3 arguments: (1) a float and (2) & (3) integers specifying the desired quanitity of intergers to be selected before and after the decimal respectively. 
# - The function should return a float truncated appropiately based on the specified digits

def before_after_dot(f, before, after):
    s = str(f)
    i = s.index('.')
    return s[i-before:i+after+1]


## 3.2 ############################################################################################################
# Exercise - Utilize the Decimal class for precise calculations
# - Accept two strings of numbers.
# - Turns them into decimals.
# - Return a float representing the sum of these two.

from decimal import Decimal

def decimal_add(first, second):
    return float(Decimal(first) + Decimal(second))

decimal_add('1.1', '1.2')


## 4 ############################################################################################################

def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

## 4.1 ############################################################################################################
# Exercise - Print decimal equivalent of hexadecimal input
# - Use the built-in "ord" and "chr" function instead of "int"

#def ord_hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87

        decnum += dec_digit * (16 ** power)
    print(decnum)


## 4.2 ############################################################################################################
# Exercise - Produce a name triangle
# -Ask the user for theirn name and produce a nname triangle.
# - Take the first letter of their name, then the first two letters, then the first
# three, and so forth.

def name_triangle():
    name = input("Enter your name: ")

    for i in range(len(name)):
        print(name[:i+1])