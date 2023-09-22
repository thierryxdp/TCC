def substitui(s,x,i):
    """ Retorna s, mas com o elemento da posicao i substituido por x
    str, int, int -> str"""
    return s[0:i] + x + s[i + 1:]