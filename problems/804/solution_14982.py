#Start your python function here
def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original e na mesma ordem que eles apareceram. tupla->tupla'''
    a=()
    if tupla[0]%2==0:
        a = a + (tupla[0],)
    elif tupla[1]%2==0:
        a = a + (tupla[1],)
    elif tupla[2]%2==0:
        a = a + (tupla[2],)
    elif tupla[3]%2==0:
        a = a + (tupla[3],) 
    return a