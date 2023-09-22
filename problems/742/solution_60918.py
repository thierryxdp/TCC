def substitui(s,x,i):
    """Retorna uma string igual a s, porém ela substitui o caractere da 
    da posição i pelo caractere x;
    str, str, int -> str"""
    l = i+1 
    return s[0:i]+x+s[l:]