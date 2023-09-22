#Start your python function here
def filtra_pares((n1,n2,n3,n4)):
    '''Retorna uma tupla apenas com os números pares dentre
       os quatro inteiros n1, n2, n3 e n4 da tupla de entrada;
       tuple -> tuple'''
    tuplaRetorno=()
    if n1%2==0:
        tuplaRetorno+=(n1,)
    if n2%2==0:
        tuplaRetorno+=(n2,)
    if n3%2==0:
        tuplaRetorno+=(n3,)
    if n4%2==0:
        tuplaRetorno+=(n4,)
    return tuplaRetorno