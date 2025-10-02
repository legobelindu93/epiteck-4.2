text = input("Please enter une chaine de chraractere: ")

firt_char = (word[0] for word in text.split())

print("".join(firt_char).upper())

