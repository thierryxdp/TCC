def faltante(Lista_L):
    '''funçao que calcula e retorna o numero que pertence ao intervalo,mas nao pertence à lista_L. list->int'''
    list.sort(Lista_L)
    proximo = 1
    if len(Lista_L) == Lista_L[-1]:
        return Lista_L[-1] + 1
    while Lista_L[proximo - 1] == proximo :
        proximo = proximo + 1
    return proximo