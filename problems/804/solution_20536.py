def filtra_pares (tup):
    '''função que recebe uma tupla com quatro elementos 
    inteiros como argumento e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original'''
    return tup[0:4].endswith('0') or tup[0:4].endswith('2') or tup[0:4].endswith('4') or tup[0:4].endswith('6') or tup[0:4].endswith('8')