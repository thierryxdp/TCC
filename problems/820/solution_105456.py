def posLetra (s,l,n):
    """retorna em que posição da string aquela ocorrência da letra está, caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    pos=-1
    if l not in s or n>s.count(l):
        return pos
    else:
        while n!=0:
            n=n-1
            pos=str.find(s,l,pos+1)
    return pos