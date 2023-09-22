def filtra_pares(a, b, c, d):
    """a funçao recebe quatro elementos inteiros e retorna apenas os que forem pares"""
    """entrada: tupla(int, int, int, int)"""
    """saida: tupla(int, int, int, int)"""
    if a,b,c,d%2==0:
        return a, b, c, d
    else: 
        return a+b+c+d