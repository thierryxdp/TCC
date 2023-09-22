def substitui(s,x,i):
    """Dado uma string s, um caractere qualquer x e um valor i que tem limite até o comprimento da string, substitui o elemento da posição i por x. str -> str"""
    return s[:i]+x+s[i+1:]