def filtra_pares(t):
    """Funcao que recebe uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam,
    tupla -> tupla"""
    tv = tuple()
    
    if t[0] % 2 == 0:
        tv = tv + (t[0],)
    if t[1] % 2 == 0:
        tv = tv + (t[1],)
    if t[2] % 2 == 0:
        tv = tv + (t[2],)
    if t[3] % 2 == 0:
        tv = tv + (t[3],)
        
        return tv