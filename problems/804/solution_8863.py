def filtra_pares(s: int):
    """recebe uma tupla com quatro elementos inteiros e 
    retorna uma nova tupla contendo apenas os elementos da tupla
    original """
    input = []
    
        if s[0:3] % 2 == 0:
            return s[0]