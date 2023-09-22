def substitui(s,x,i):
    """funcao que substitui um caractere x na posicao i de uma string s
    str, str, int -> str"""
    
    return s[0:i] + x + s[i+1:]