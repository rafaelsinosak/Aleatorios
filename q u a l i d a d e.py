texto = input ("Texto: ")
caractere = input ("Caractere: ")
textofinal=caractere+""
for x in range (len(texto)):
    textofinal+=str(texto[x].upper()+" ")
textofinal=textofinal[:-1]
textofinal+=str(caractere)
print (textofinal)    
