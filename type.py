import string, sys, os, re, time, colorama
from colorama import Fore
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

colorama.init()

check_chars = set("abcdefghijklmnopqrstuvwxyz,.!? ")

for char in text:
    
    if char not in check_chars:
        print(Fore.GREEN + char, end="")
    else:
        for letter in check_chars:
            if char != letter:
                print(letter, end="\b")
                time.sleep(0.01)
            else:
                print(Fore.GREEN + char, end="")
                break