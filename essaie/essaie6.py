print("le but du jeu est très simple, il suffit de choisir un chiffre de 1 à 1000000. si le chiffre que vous avez choisis s'affiche à l'écran, vous avez gagnez!!!")

import random

r= random. randint(1, 1000000)
print("qu'est-ce que tu choisis")
a=input()
print(r)
if (a == r): 
    print("WOW, T'ES LE MEILLEUR!!!!!!!!!")
else : 
    print ("désolé, vous n'avez pas réussis")

