def filtra_pares(s: int):
    """recebe uma tupla com quatro elementos inteiros e 
    retorna uma nova tupla contendo apenas os elementos da tupla
    original """
    
    tp1 = ()
        
    if s[0] % 2 == 0: tp1 = tp1 + (s[0],)     
    if s[1] % 2 == 0: tp1 = tp1 + (s[1],)
    if s[2] % 2 == 0: tp1 = tp1 + (s[2],)
    if s[3] % 2 == 0: tp1 = tp1 + (s[3],)
    return tp1