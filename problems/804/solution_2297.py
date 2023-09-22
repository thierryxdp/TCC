def filtra_pares(tup):
    """Recebe um conjunto de quatro números (inteiros) e retorna uma nova tupla, que é
    o conjunto contendo apenas os elementos pares do conjunto original

    Parâmetros: tup -> tupla
    Retorno: <tuplar> -> tupla"""
    tuplar = ''
    if (tup[0]%2 == 0):
        tuplar = tuplar + str(tup[0])
    if (tup[1]%2 == 0):
        tuplar = tuplar + str(tup[1])
    if (tup[2]%2 == 0):
        tuplar = tuplar + str(tup[2])
    if (tup[3]%2 == 0):
        tuplar = tuplar + str(tup[3])
    return tuplar