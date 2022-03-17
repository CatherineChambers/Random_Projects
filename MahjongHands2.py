import re
from collections import Counter
from typing import Any

import numpy


def mahjong_shanten():
    tiles_in_suit: dict[str | Any, str | list[Any] | list[list[Any]]] = {
        "manzu": "m",
        "pinzu": "p",
        "souzu": "s",
        "jihai": "z"
    }
    hand = input("Please input a starting hand:")
    shanten_count = 0

    # ----------------------------
    hand = re.sub(r"([^\dmpsz])", "", hand)  # Remove unwanted characters from input
    digits_only = re.sub(r"([^\d])", "", hand)
    if len(digits_only) != 14:
        raise Exception("Please input a valid starting hand of 14 tiles.")
    # Need to check that the number of individual tiles is < 5

    # Reorder and separate suit tiles. Create a list of suit tiles, sorted in tile_in_suit dict.
    for name, item in tiles_in_suit.items():
        # Group numerical characters into the dictionary so that each suit is separate.
        tiles_in_suit[name] = re.findall(r"(\d+)" + item, hand, flags=re.IGNORECASE)
        # Reformat string so that each digit is an element of a list in numerical order.
        tiles_in_suit[name] = [list(item) for item in tiles_in_suit[name]]
        tiles_in_suit[name] = [item for sublist in tiles_in_suit[name] for item in sublist]
        tiles_in_suit[name] = sorted(tiles_in_suit.values[name])
        print(tiles_in_suit[item])

    print(tiles_in_suit.values())

    for name in tiles_in_suit.keys():
        if len(tiles_in_suit[name]) > 0:
            tiles_list = [int(i) for i in tiles_in_suit[name]]
            tiles_list_diff = numpy.diff(tiles_list)  # The difference between each value in the tuple
    print(tiles_in_suit)


mahjong_shanten()
