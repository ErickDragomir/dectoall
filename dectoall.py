#imports
import sys
import os
#ASCII text Title

class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(color.HEADER)
print(' 8888888b.  8888888888 .d8888b.       888                        d8888 888      888         ')
print(' 888  "Y88b 888       d88P  Y88b      888                       d88888 888      888         ')
print(' 888    888 888       888    888      888                      d88P888 888      888         ')
print(' 888    888 8888888   888             888888 .d88b.           d88P 888 888      888         ')
print(' 888    888 888       888             888   d88""88b         d88P  888 888      888          ___     ___ ')
print(' 888    888 888       888    888      888   888  888        d88P   888 888      888         |_  |   |   |')
print(' 888  .d88P 888       Y88b  d88P      Y88b. Y88..88P       d8888888888 888      888          _| |_ _| | |')
print(' 8888888P"  8888888888 "Y8888P"        "Y888 "Y88P"       d88P     888 88888888 88888888    |_____|_|___|')
print("Version 1.0 by ErickDragomir")
print("" + color.ENDC)



print("[USED OS: " + sys.platform + " ]")
print("[OS VERSION: " + sys.version + " ]")

print(" ")


#number input
number = int(input("Insert number: "))
print(" " + color.GREEN)

#print selected number
print(str("DEC: ") + str(number))
print(" " )

#DEC to BIN
bin = bin(number)
print("BIN: " + bin)
print(" ")

#DEC to HEX
hex = hex(number)
print("HEX: " + hex)
print(" ")

#DEC to OCT
oct = oct(number)
print("OCT: " + oct)
print(" " + color.ENDC)

input("Press any key to continue...")
