def stutter(word):
    return word[:2] + "... " + word[:2] + "... " + word + "?"


def stutter2(word):
    return "{0}... {0}... {1}?".format(word[:2], word)
