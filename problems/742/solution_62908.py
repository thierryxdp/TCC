def substitui(s,x,i):
    """substitui o caractere x na posição i da palabra s
    str,str,int -> str"""
    return (s[0:i]+x)+(s[i+1:])