def filtra_pares(t):
    def resto(a, b):
        return a % b
    
    def eh_par(n):
        return resto(n, 2) == 0
    
    def eh_impar(n):
        return not eh_par(n)

    ret = list(t)
    for item in ret:
        if eh_impar(item):
            ret.remove(item)
    return tuple(ret)