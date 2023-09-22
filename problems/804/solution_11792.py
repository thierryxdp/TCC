def filtra_pares(tupla):
    '''funcao que filtra numeros pares dada
    uma tupla como parametro'''
    pares= ([tupla]%2==0)
    impares= ([tupla]%2==1)
    return pares