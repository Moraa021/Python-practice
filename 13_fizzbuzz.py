"""
Problem: Print numbers from 1 to n. For multiples of 3, print "Fizz".
For multiples of 5, print "Buzz". For multiples of both, print
"FizzBuzz".

Input:  n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
         "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

Concepts: loops, conditionals, modulo operator
"""


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    # Normal case
    print(fizzbuzz(15))
    # Edge cases: n = 0, n = 1
    print(fizzbuzz(0))
    print(fizzbuzz(1))
