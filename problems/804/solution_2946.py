#Start your python function here
def filtra_pares (tupla):
    """ Transforma uma tupla em uma nova tupla somente com números pares. 
    entrada:tupla com elementos inteiros
    saida: tupla com elementos inteiros pares
    """
    pares= ()
    if tupla [0] % 2 == 0:
        pares = (tupla[0], )
    if tupla[1]%2==0:
        pares= pares+(tupla[1], )
    if tupla[2]%2==0:
        pares= pares+(tupla[2], )
    if tupla[3]%2==0:
        pares= pares+(tupla[3], )
    return pares