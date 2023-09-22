def substitui(s,x,i):
    """calcula uma função dada um string, um caractere e um numero inteiro 
    e retorna uma string igual, exeto que o elemento da posiçao  i é substituido pelo caractere x;
    str, str, int--str"""
    F = s[0:i] + x
    if s[i] == s[-1] and (i + 1) != len(s):
        return F + s[(1+i):-1] + s[-1]
    elif s[i] == s[-1]:
        return F
    elif s[i] != s[-1]:
        return F + s[(1+i):-1] + s[-1]