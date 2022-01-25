import sys
import os

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
#ASCII text Title

print( color.HEADER + "DEC TO ALL - Android friendly .py file for terminal like termux")
print( color.ENDC + "Version 1.0 by ErickDragomir")
print(" ")



print("[USED OS: " + sys.platform + " ]")
print("[OS VERSION: " + sys.version + " ]")

print(" ")


#number input
number = int(input("Insert ONLY number: "))
print(color.GREEN)

#print selected number
print(str("DEC: ") + str(number))
print(" ")

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
print( color.ENDC )

input("Press any key to continue...")

