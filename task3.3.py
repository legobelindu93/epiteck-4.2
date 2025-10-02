numero_un = input("choisie un premier nombre. ") # demande le numero de l'utilisateur et le stocke dans la variable numero
numero_deux = input("choisie un deuxieme nombre. ") # demande le numero de l'utilisateur et le stocke dans la variable numero
numero = sum ([int(numero_un), int(numero_deux)]) # convertit le numero en entier et le stocke dans la variable numero
print("The sum of the provided numbers is " + str(numero)) # affiche le resultat de la somme des deux nombres