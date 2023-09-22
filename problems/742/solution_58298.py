def substitui(s,x,i):
    """essa função substitui uma string por ela mesma, porém com o caractere da posição (i) substituido pelo caractere (x);
    str,str,int--->str"""
    s = list(s)
    s[i] = x
    return ''.join(s)