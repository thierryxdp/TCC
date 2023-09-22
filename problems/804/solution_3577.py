#Start your python function here
def filtra_pares(tupla):
    '''funcao que recebe uma tupla com 4 elementos e retorna uma nova tupla apenas com os elementos pares
       da tupla original, na mesma ordem em que se encontravam.
       tuple -> tuple'''
    i = 0
    if(tupla[0]%2 == 0):
        pares[i] = tupla[0]
        i = i+1
    if(tupla[1]%2 == 0):
        pares[i] = pares + tupla[1]
        i = i+1
    if(tupla[2]%2 == 0):
        pares[i] = pares + tupla[2]
        i = i+1
    if(tupla[3]%2 == 0):
        pares[i] = pares + tupla[3]
        i = i+1
    return pares