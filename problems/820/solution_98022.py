def posLetra(f,l,q):
    """Retorna em que posição da string a ocorrencia da letra está, caso tenha 
    menos ocorrencias da letra do que a ocorrencia perdida retorna -1
    str,str,int -> int"""
    x = 0
    i = 0
    k = f.count(l)
    if k < q:
        return -1
    else:
        while q != x:
            if f[i] == l:
                x += 1
            i += 1
        return i-1