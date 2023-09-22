def filtra_pares(s: int):
    """recebe uma tupla com quatro elementos inteiros e 
    retorna uma nova tupla contendo apenas os elementos da tupla
    original """
    input = []
    
    if s[0] % 2 == 0:
        return s[0]
    
    elif s[1] % 2 == 0:
        return s[1]
    
    elif s[2] % 2 == 0:
        return s[2]

    elif s[3] % 2 == 0:
        return s[3]