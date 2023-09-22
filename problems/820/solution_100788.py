def posLetra(s,l,n):
    """retorna a posiçao da ocorrencia n da letra l na string s"""
    """str, str, int -> int"""
    i = 1
    x = s.find(l)
    if n <= s.count(l):
        while i < n:
            x = s.find(l,x+i)
            i += 1
            return x
    else:
        return -1