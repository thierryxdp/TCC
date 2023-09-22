def substitui(s,x,i):
    """dado uma string s, troca o elemento de posicao i
    pelo caractere x dado
    str, str, int -> str"""
    i2=i+1
    return s[0:i] + x + s[i2:]