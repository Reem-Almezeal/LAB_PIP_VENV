from art import text2art
from colorama import Fore, Back, Style, init

init(autoreset=True)

text1 = text2art("BELIEVE AND ACHEIVE", font="block")
print(Fore.GREEN + text1)

text2 = text2art("HELLO", font="sub-zero")
print(Back.MAGENTA + Style.BRIGHT + text2)


text3=text2art("REEM","rnd-xlarge")
print(Back.LIGHTBLUE_EX + Style.DIM + text3)

text4=text2art("REEMAlmezeal",font="rnd-large")
print(Fore.CYAN + Style.NORMAL + text4)