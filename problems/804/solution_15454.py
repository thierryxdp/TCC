#Start your python function here
def filtra_pares(tuplaEntrada):
    '''Retorna uma tupla apenas com os números pares dentre
       os quatro inteiros n1, n2, n3 e n4 da tupla de entrada;
       tuple -> tuple'''
    n1=tuplaEntrada[0]
    n2=tuplaEntrada[1]
    n3=tuplaEntrada[2]
    n4=tuplaEntrada[3]
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