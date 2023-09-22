def substitui(s, x, i):
    """Retorna a string igual a str, com elemento da posição i substituido pelo x
       str,str,int --> str"""
    
    return s[0:i] + x + s[i + 1:]