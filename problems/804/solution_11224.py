def filtra_pares(a, b, c, d):
    """essa funçao recebe uma tupla com quatro elementos e retorna somente os pares"""
    """entrada: tupla(int, int, int, int)"""
    """saida: tupla(int, int, int, int)"""
    if filtra_pares[0]%2==0:
        return a
    if filtra_pares[1]%2==0:
        return b
    if filtra_pares[2]%2==0:
        return c
    if filtra_pares[3]%2==0:
        return d
    return filtra_pares(a, b, c, d)%2