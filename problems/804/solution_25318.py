def par(n):
    '''Retorne true se n for um número par e false se n for um número ímpar. int/float -> bool'''
    return n%2==2

def filtra_pares(tupla):
    ''' Receba uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam. tup->tup'''
    pares=()
    
    if par(tupla[0]):
       pares = pares + (tupla[0],)
    if par(tupla[1]):
       pares = pares + (tupla[1],)
    if par(tupla[2]):
       pares = pares + (tupla[2],)
    if par(tupla[3]):
       pares = pares + (tupla[3],)
    return pares