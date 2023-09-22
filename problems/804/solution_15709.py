def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com 4 elementos inteiros
    e retorna uma nova tupla contendo apenas os elementos
    pares da tupla original
    tupla(int,int,int,int) -> tupla"""
    t=(a,b,c,d)
    sub=()
    if(a%2==0):
        sub=t[0]
    if(b%2==0):
        sub=sub+t[1]
    if(c%2==0):
        sub=sub+t[2]
    if(d%2==0):
        sub=sub+t[3]
    return sub