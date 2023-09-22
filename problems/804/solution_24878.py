def filtra_pares(t):
    """Recebe como parâmmetro uma tupla contendo 4 números inteiros e retorna uma
    nova tupla contendo apenas os número pares da tupla original, na mesma ordem em que se encontravam.
    assinatura: tuple(int, int, int, int) --> tuple(...)
    casos de teste:
    filtra_pares( (1, 2, 3, 4) ) == (2, 4)
    filtra_pares( (4, 3, 2, 1) ) == (4, 2)
    filtra_pares( (0, 0, 0, 0) ) == (0, 0, 0, 0)
    filtra_pares( (0, 1, 0, 1) ) == (0, 0)
    """
    def resto(a, b):
        return a % b

    def eh_par(n):
        return resto(n, 2) == 0
    
    ret = []
    
    if eh_par(t[0]):
        list.append(ret, t[0])
    if eh_par(t[1]):
        list.append(ret, t[1])
    if eh_par(t[2]):
        list.append(ret, t[2])
    if eh_par(t[3]):
        list.append(ret, t[3])
    return tuple(ret)