# 8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/, https://acmp.ru
# И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.


# codewars.com, 7 kyu
# Remove all of the vowels from string
# Note: for this kata "y" isn't considered a vowel.
def disemvowel(string_):
    for elem in string_:
        if elem in "aoeuiAOEUI":
            string_ = string_.replace(elem, "")
    return string_


# hackerrank.com, easy
# The provided code stub reads and integer, n, from STDIN.
# For all non-negative integers i < n, print i in square.
if __name__ == '__main__':
    n = int(input())

if n:
    for elem in range(0, n):
        print(elem ** 2)


# hackerrank.com, easy
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
#   If n is even and in the inclusive range of 2 to 5, print Not Weird
#       If n is even and in the inclusive range of 6 to 20, print Weird
#           If n is even and greater than 20, print Not Weird
if __name__ == '__main__':
    n = int(input().strip())

if (n % 2) or (not n % 2 and n in range(6, 21)):
    print("Weird")
elif (n > 20) or (not n % 2 and n in range(2, 6)):
    print("Not Weird")


# hackerrank.com, medium
# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.
# In the Gregorian calendar, three conditions are used to identify leap years:
#   The year can be evenly divided by 4, is a leap year, unless:
#       The year can be evenly divided by 100, it is NOT a leap year, unless:
#           The year is also evenly divisible by 400. Then it is a leap year.
def is_leap(year):
    leap = False

    if (not year % 4) and (year % 100) or (not year % 400):
        leap = True

    return leap


year = int(input())
print(is_leap(year))
