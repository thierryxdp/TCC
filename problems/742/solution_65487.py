def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i e retorna a mesma string s porém com o elemento da posição i substituído por x'''
    string = s
    0 < i < len(s)
    return s[:i] + str(x) + s[i:]