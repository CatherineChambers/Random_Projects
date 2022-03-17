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
