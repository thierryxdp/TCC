#Start your python function here
def filtra_pares(tupla):
    '''funcao que recebe uma tupla com 4 elementos e retorna uma nova tupla apenas com os elementos pares
       da tupla original, na mesma ordem em que se encontravam.
       tuple -> tuple'''
    pares = (0,)
    i = 0
    if(tupla[0]%2 == 0):
        pares = tupla[0]
    if(tupla[1]%2 == 0):
        pares = pares + tupla[1]
    if(tupla[2]%2 == 0):
        pares = pares + tupla[2]
    if(tupla[3]%2 == 0):
        pares = pares + tupla[3]
    return pares