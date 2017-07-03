# Fizzbuzz tests
from assertions import assertEqual, printErrors
from FizzBuzz import FizzBuzz

assertEqual("Fizz", FizzBuzz(3))
assertEqual("Buzz", FizzBuzz(5))
assertEqual("FizzBuzz", FizzBuzz(15))
assertEqual("X", FizzBuzz(1))

printErrors()