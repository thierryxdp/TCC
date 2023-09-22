#Start your python function here
def filtra_pares (notas):
    '''
    Função que recebe uma tupla de quatro elementos inteiros
    e retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original
    Tuple--->tuple
    '''
    x, y, z, w = notas
    tupla_final = tuple()

    if x % 2 == 0:
        tupla_final += (x, )

    if y % 2 == 0:
        tupla_final += (y, )

    if z % 2 == 0:
        tupla_final += (z, )

    if w % 2 == 0:
        tupla_final += (w, )

    return tupla_final