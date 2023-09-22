def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos inteiros como parâmetro, e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original'''
    lista = list
    for x in tupla:
        if x // 2 == 1 or x == 0:
            lista.append(x)
    return lista