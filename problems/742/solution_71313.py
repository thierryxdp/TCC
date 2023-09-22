def substitui(s,x,i):
    """retorna uma string 's' substituindo um caractere localizado em 'i'por um caractere 'x'.
    str,int,int -> str"""
    c=s[i]
    return s[0,i] + c + [i+1,]