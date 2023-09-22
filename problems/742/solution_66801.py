def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i e retorne uma string igual a s, porém com o elemento da posição i substituido por x'''
    0 < i < len(s)
    return s[:i] + str(x) + s[i:]