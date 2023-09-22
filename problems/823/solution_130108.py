def faltante(listaPecas):
    '''Identifica e retorna o valor numérico da peça que falta na lista;
    list -> int'''
    list = []
    i = 0
    listaPecas.sort()
    while i < (len(listaPecas)-1):
        if listaPecas[i+1] - listaPecas[i] > 1:
            return i + 2
        i += 1
    if listaPecas[0] == 1:
        return listaPecas[-1] + 1
    else:
        return listaPecas[0] - 1