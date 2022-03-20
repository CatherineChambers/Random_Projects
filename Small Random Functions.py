#  Length of a number

def number_length(num):
    string_num = str(num)
    return 1 + number_length(string_num[1:]) if string_num else 0


# Stuttering Function

def stutter(word):
    return word[:2] + "... " + word[:2] + "... " + word + "?"


def stutter2(word):
    return "{0}... {0}... {1}?".format(word[:2], word)


# Simplified proper fractions

def compute_gcd(a, b):
    gcd = 0
    for i in range(1, min(a, b) + 1):
        if not a % i and not b % i:
            gcd = i
    return gcd


def sim_prop_fraction(max_den):
    denominator = max_den
    fraction_number = 0
    while denominator > 1:
        num_range = range(1, denominator)
        for numerator in num_range:
            if compute_gcd(numerator, denominator) == 1:
                fraction_number += 1
        denominator -= 1
    return fraction_number
