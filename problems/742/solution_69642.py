def substitui(s,x,i):
    """dada uma string, um caractere x e um numero i entre 0 e o comprimento da string retorna
    a string s, com o elemento da posição i substituido por pelo caractere x.
    str, str, int --> str"""
    s1=s[0:i]
    s2=s1+x+s[i+1:len(s)]
    return s2