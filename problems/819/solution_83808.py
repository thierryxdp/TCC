def filtraMultiplos(lista_numeros, n):
    '''
       Dado uma lista de números e um
       número n, a função retorna uma
       nova lista apenas com os números
       que são divisíveis por n
    '''
    i=0
    d=n
    while lista_numeros[i]%d==0:
        i = i + 1
        d = d + 1
    return i