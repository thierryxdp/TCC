def total(lista,dicionario):
    total=0
    indice=0
    while lista[indice] < len(lista):
        total= total + dict.get(dicionario,lista[indice])
        indice +=1
    return total