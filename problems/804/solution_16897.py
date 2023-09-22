def filtra_pares(x:int,y:int,w:int,z:int)->tuple:
    tupla = ()
    if (x % 2) == 0:
        tupla += ([x],)
    if (y % 2) == 0:
        tupla += ([y],)
    if (w % 2) == 0:
        tupla += ([w],)
    if (z % 2) == 0:
        tupla += ([z],)
        return tupla