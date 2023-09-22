def faltante(lista):
    ''' funcao que recebe um intervalo de numeros correpondentes ao numero de pecas e retorna o numero/peca faltante. list -> int'''
    indice = 1
    while indice < len(lista):
        if len(lista) != 1 and (lista[indice] - lista[indice - 1]) != 1:
            return (lista[indice] + lista[indice - 1])/2
        if len(lista) != 1 and (lista[indice] - lista[indice - 1]) == 1:
            indice += 1
        if len(lista) != 1 and 1 != lista[0]:
            return 1
        if (len(lista)+1) != lista[-1]:
            return len(lista) +1
        if len(lista) == 1 and lista[0] > 1:
            return 1
        if len(lista) == 1 and lista[0] == 1:
            return 2