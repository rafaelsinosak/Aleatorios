interrogacao="?"
for x in range (0,15):
    print (interrogacao)
    interrogacao+=str("?")
for x in range (1,17):
    print (interrogacao[0:-x])
