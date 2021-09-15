#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
This little program calculates the weight of a steel sheet by using class for the calculation.
"""
__author__ = "Zsolt Peto"
__license__ = "MIT"
__copyright__ = "Copyright 2021"
__version__ = "0.2"
__status__ = "In progress"

from sys import argv, exit


def usage():
    print(f"Wsheet {__version__}")
    print(f"{__copyright__} {__author__}\n")
    print("Usage:\n> ./Wsheet.py 3000 1500 2 or 2.0\n")
    exit()


def helpmessage():
    print("-h or --help    - Print this screen")
    print("-v or --version - Print a program version\n")


if len(argv) <= 1:
    usage()

if argv[1] == "-v" or argv[1] == "--version":
    print(f"Wsheet version {__version__}\n")
    exit()
elif argv[1] == "-h" or argv[1] == "--help":
    helpmessage()
    exit()
elif len(argv) < 4:
    print("\nMissing dimensions!\n")
    helpmessage()
    usage()

try:
    width = int(argv[1])
    length = int(argv[2])
except ValueError:
    print("\nShould be integer the dimension!\n")
    usage()

try:
    thick = float(argv[3])
except ValueError:
    print("\nShould be float the dimension!\n")
    usage()


class Wsheet:
    """Calculated the weight of sheet metal."""

    def __init__(self, wi=0, le=0, th=0.0):
        """
        width: The width of the sheet. Should be integer. Default is 0.
        length: The length of the sheet. Should be integer. Default is 0.
        thick: The thickness of the sheet. Should be integer. Default is 0.
        Default density is 7.85 g/cm3.
        """
        self.width = wi
        self.length = le
        self.thick = th
        self.dens = 7.85
        self.weight = 0.0

    def calcweight(self):
        """Calculate the weight."""
        self.weight = ((self.width * self.length * self.thick * self.dens) / 10 ** 6)

    def getweight(self):
        """Prints the calculated weight."""
        if self.weight < 1:
            self.weight = self.weight * 10 ** 3
            print("Weight: {:4.2f} g\n".format(self.weight))
        else:
            print("Weight: {:4.2f} kg\n".format(self.weight))

    def getdim(self):
        """Prints the sheet metal dimension."""
        print(f"Size  : {self.width} * {self.length} * {self.thick} mm")


def main():
    w1 = Wsheet(width, length, thick)
    w1.calcweight()
    print("")
    print(w1.__doc__)
    print("")
    w1.getdim()
    w1.getweight()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Bye Bye!\n")
