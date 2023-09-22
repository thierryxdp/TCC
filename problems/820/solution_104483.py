def posLetra(s, l, n):
    """Retorna o índice da ocorrência n da letra l na string s.
    str, str, int -> int"""
    if 0 < n <= s.count(l):
        i = 0
        while n > 0:
            i = s.find(l, i)
            n -= 1
        return i
    return -1