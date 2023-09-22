def total(lista,dicionario):
    total=0
    indice=0
    while indice < len(lista):
        total= total + dict.get(dicionario,lista[indice])
        indice +=1
    return total