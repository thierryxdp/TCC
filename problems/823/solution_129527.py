def faltante(lista):
    listaNova=[]
    for x in range(1,len(lista)+2):
        listaNova.append(x)
    for elementoFaltando in listaNova:
        if elementoFaltando not in lista:
            return elementoFaltando