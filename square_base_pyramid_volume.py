#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program calculates the volume of a square-based pyramid

import math


def main():
    print("To calculate the volume of a square based pyramid:")
    print()

    base_length = float(input("What is the base length in cm?"))
    base_width = float(input("What is the base width in cm?"))
    height = float(input("What is the height in cm?"))
    volume = base_length * base_width * height / 3

    print("\nVolume: {} cm³".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
