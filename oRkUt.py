var=input("Texto: ")
tamanho=len(var)
texto=""
for x in range (tamanho):
        if (x%2==0):
            texto+=str(var[x].upper())
        else:
            texto+=str(var[x].lower())
print (texto)
