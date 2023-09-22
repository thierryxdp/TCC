def substitui(s,x,i):
    """Dada uma String S, um caractere x e um int i
    que esteja entre as posições possiveis na string.
    Retorna uma string s com o elemento em i substituido por x."""
    string_nova = s[0:i] + x + s[i+1:len(s)]
    return string_nova