#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autumn assignment - SETU cybersecurity - Programming I
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

import argparse
import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

__author__ = "Alberto Oesterle"
__copyright__ = "Copyright 2022, SETU / ITCarlow"
__licence__ = "<LICENCED under GNU General Public License v3.0>"
__version__ = "Version: 1.0.0"
__program__ = sys.argv[0][2:] if (sys.argv[0][:2] == "./") else sys.argv[0]
OTHER = "Autumn assignment - Alberto Oesterle for Declan Ó Briain, written \
in Visual Studio Code Version 1.72.2"

# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //            other() Function            // #
# -------------------------------------------- #


def other(other_):
    """<OTHER>() function"""

def other(other_):
    fun_name = "<OTHER>()"
    return f"{fun_name}: {other_} STUFF HERE>"


# End <OTHER>() function

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #


def main(nspace):
    """main() function"""

    arg_ = sys.argv[1:]

    list_A = ["Author", "Copyright", "License"]
    list_B = [__author__, __copyright__, __licence__]

    tl = len(max(list_A, key=len)) + 2

    if (arg_) == ['-l'] or ['--licence'] or ['--license']:
        print("\n")

        for a in range(0,3):
           print(f"{list_A[a] : <{tl}}: {list_B[a]}")
        
        sys.exit(1)

    # // Print program name //
    print(__doc__)

    # // Arguments from shell //
    print(f"namespace: '{nspace}'")

    # // Arguments from shell as dictionary //
    print(f"dictionary: '{vars(nspace)}'")

    # // Arguments from shell //
    print("main() action: 'print from main()'")

    # // call <OTHER_FUNCTION>() //
    print("print from other()", other("OTHER"))


# End main() function


# ============================================ #
# //                  Global                // #
# ============================================ #

# // Command line parsing //
parser = argparse.ArgumentParser(description=f"{__program__} Ip Address pinger \
Program")

parser.add_argument(
    "-l", "--licence", help=f"{__program__} licence information",
    required=False, action='store_true'
)
parser.add_argument(
    "-v", "--version", help=f"{__program__} version information",
    action='version', version=__version__
)
parser.add_argument(
    "-i", "--IP", help="IP address list",
    required=False, action='append'
)
parser.add_argument(
    '--license', help=argparse.SUPPRESS, required=False, action='store_true'
)


# // Call main function (Pick minimum version if necessary) //
if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor >= 0:
        main(parser.parse_args())
    else:
        print("A python version greater that 3.0 is required.")
else:
    sys.exit(1)
