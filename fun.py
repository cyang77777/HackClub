import pyfiglet
T = input("Enter Text you want to convert to ASCII art : ")
ASCII_art_1 = pyfiglet.figlet_format(T,font='isometric1')
print(ASCII_art_1)