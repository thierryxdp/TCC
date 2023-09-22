def filtra_pares(tupla):
    """Recebe uma tupla, com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla
    original, na mesma ordem em que se encontravam;
    tuple -> tuple"""
    tupla_par = ()
    if(tupla[0] % 2 == 0):
        tupla_par = tupla[0]
    if(tupla[1] % 2 == 0):
        tupla_par = tupla[1]
    if(tupla[2] % 2 == 0):
        tupla_par = tupla[2]
    if(tupla[3] % 2 == 0):
        tupla_par = tupla[3]
    return tupla_par