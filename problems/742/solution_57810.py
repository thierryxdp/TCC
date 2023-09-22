def substitui(s,x,i):
    """substitui o caractere na posição i, pelo caractere inserido em x
    entrada:str,str,int
    saida:string"""
    
    z=s[:i]+x+s[i+1:]
    return z