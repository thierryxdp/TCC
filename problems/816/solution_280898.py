def maiores(lista, n):
    '''Essa função recebe uma list de numeros 'lista' e um numero 'n', a partir disso
    ela insere n em lista e após isso ordena ela de forma crescenbte,
    depois disso ela procura o indice referente a n e retorna uma fatia de lista
    da posição do primeiro numero maior que n em diante
    list, int ------->list'''
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    return lista[indice+1:]