def insere(list_numero,n):
    '''
    Função de uma lista ordenada que coloca o numero(n) na posição correta
    list -> list
    '''
    list.insert(list_numero,0,n)
    list.sort(list_numero)
    return list_numero