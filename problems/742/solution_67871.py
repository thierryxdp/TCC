def substitui(s,x,i):
    """função definida por substitui(s, x, i) que receba uma string s,
    um caractere x e um número inteiro i entre 0 e o comprimento da string,
    e retorne uma string igual a s, exceto que o elemento da posição i deve ser
    substituído pelo caractere x"""
    return str(s[:i])+str(x)+str(s[i+1:])