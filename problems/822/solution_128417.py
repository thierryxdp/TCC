def repetidos(lista):
    contador = 0
    teste = 0
    listnum = str(lista)
    while contador<len(listnum):
        if listnum[contador]==listnum[contador-1]:
            teste = teste+1
        contador = contador +1
    return teste