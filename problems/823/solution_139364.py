def faltante(lista):
    ''' funcao que recebe um intervalo de numeros correpondentes ao numero de pecas e retorna o numero/peca faltante. list -> int'''
    lista_ordenada = lista.sort()
    indice = 1
    while indice < len(lista):
        if (lista[indice] - lista[indice - 1]) != 1:
            return (lista[indice] + lista[indice - 1])/2
        if (lista[indice] - lista[indice - 1]) == 1:
            indice += 1