def substitui(s,x,i):
    """substitui o caractere na posição i, pelo caractere inserido em x
    entrada:str,str,int
    saida:string"""
    c=s[:i]
    z=c+x+s[i:]
    return z