def insere(lista_numero,n):
    
    ''' A função recebe uma lista ordenada de numeros int e um numero int aleatório,
        junta o numero aleatório com a lista e gera uma nova lista ordenada;
        list, int -> list
    '''

    lista_junta = lista_numero + [n]

    return sorted(lista_junta)


def maiores(lista_numero,n):

    junta_listas = sorted(lista_numero + [n])

    x = junta_listas.index(n)

    return junta_listas[x:]