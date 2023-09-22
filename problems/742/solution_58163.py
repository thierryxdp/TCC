def substitui(s,x,i):
    '''recebe uma string s, um caractere x e um numero inteiro i, retornando uma string igual a s, trocando o elemento da posição i com o caracter x'''
    0 < i < len(s)
    return s[0;i] + x + s[i:]