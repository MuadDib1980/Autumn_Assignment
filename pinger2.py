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
import platform
import subprocess as sp
import ipaddress

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

__author__ = "Alberto Oesterle"
__copyright__ = "Copyright 2022, SETU / ITCarlow"
__licence__ = "<European Union Public Licence v1.2>"
__version__ = "Version: 1.0.0"
__program__ = sys.argv[0][2:] if (sys.argv[0][:2] == "./") else sys.argv[0]
OTHER = "Autumn assignment - Alberto Oesterle for Declan Ó Briain, written \
in Visual Studio Code Version 1.72.2"

# ============================================ #
# //                Functions               // #
# ============================================ #

def ipchecker(ip_):
    try:
        ip_object = ipaddress.ip_address(ip_)
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, '1', ip_]
        try:
            ipresponse = sp.check_output(command, stderr=sp.STDOUT, universal_newlines=True)
            print(f'{ip_} is alive')

        except sp.CalledProcessError:
            print(f'{ip_} is unreachable')
    except:
        print(f'{ip_} - ERROR: is not a properly formatted address')

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #

def main(nspace):
    """main() function"""

    list_A = ["Author", "Copyright", "Licence"]
    list_B = [__author__, __copyright__, __licence__]

    tl = len(max(list_A, key=len)) + 2

    if nspace.licence or nspace.license:
        print("\n")

        for a in range(0,3):
           print(f"{list_A[a] : <{tl}}: {list_B[a]}")

        print("\n")        

    elif nspace.ip:
        print("\n")
        for x in nspace.ip:
            ipchecker(x)
            
    else:
        x = input(f'Enter an IP address: ')
        ipchecker(x)
    
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
    "-i", "--ip", help="IP address list",
    required=False, nargs='+'
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
