# imports
import os
from colorama import Fore, Back, Style

# title

print(Fore.CYAN+'''
███████╗███████╗██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░
██╔════╝╚════██║██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░
█████╗░░░░███╔═╝██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░
██╔══╝░░██╔══╝░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░
███████╗███████╗██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗
╚══════╝╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
'''+Fore.BLUE+"                                                            Generator")

# input
filename = input(Fore.WHITE+'Enter your desired file name: ')
filehost = input("Enter the zip file URL: ");


# magic
