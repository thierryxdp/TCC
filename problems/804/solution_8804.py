def filtra_pares(s:int):
    input = []
    
    if s[0] % 2 == 0 and s[1] % 2 == 0:
        return s[0], s[1]