def filtra_pares(tupla):
    '''funcao que filtra numeros pares dada
    uma tupla como parametro
    entrada: tuple
    saida: tuple
    '''
    pares= tuple(tupla)%2==0
    impares= tuple(tupla)%2==1
    return tuple(pares)