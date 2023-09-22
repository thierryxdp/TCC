def filtra_pares(t):
    '''Funcao que recebe quatro valores inteiros e retorna apenas os valores pares
    tuple -> tuple'''
    tupla2 = ()
    cont = 0
    tamanho = len(t)

    while cont < tamanho:
        if t[cont]%2 == 0:
            tupla2 = tupla2 + (t[cont],)
        cont = cont + 1

    return tupla2