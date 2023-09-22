def faltante(lista):
    """ """
    indice = 0
    tamanhoLista = len(lista) + 1
    listinha = list(range(1,tamanhoLista+1))
    lista.sort()
    while indice<len(lista):
        if listinha[-1] == lista[-1]+1:
            return listinha[-1]
        if lista[indice] == listinha[indice]:
            indice += 1
        else:
            return listinha[indice]