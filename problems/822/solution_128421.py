def repetidos(lista):
    contador = 1
    teste = 0
   	listnum = lista[]
    while contador<len(listnum):
        if listnum[contador]==listnum[contador-1]:
            teste = teste+1
        contador = contador +1
    return teste