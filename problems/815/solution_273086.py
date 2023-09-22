def insere(lista_numero,n):
    
    ''' A função recebe uma lista ordenada de numeros int e um numero int aleatório,
        junta o numero aleatório com a lista e gera uma nova lista ordenada;
        list, int -> list
    '''

    lista_junta = lista_numero + [n]

    return sorted(lista_junta)