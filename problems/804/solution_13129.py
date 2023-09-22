def filtra_pares ( tupla: tuple)-> tuple:
    '''retorna uma nova tupla contendo apenas os elementos pares da tupla
    original, dada a tupla original com quatro elementos inteiros'''
    final = ()
    if tupla [0] % 2 == 0:
        final = final + (tupla[0],)
    if tupla [1] % 2 == 0:
        final = final + (tupla[1],)
    if tupla [2] % 2 == 0:
        final = final + (tupla[2],)
    if tupla [3] % 2 == 0:
        final = final + (tupla[3],)
    return final