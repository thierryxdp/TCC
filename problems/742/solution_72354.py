def substitui(s, x, i):
    '''funcao que que receba uma string s, um caractere x e um
numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, exceto que o elemento
da posicao i é substituıdo pelo caractere x'''
    n = i - 1
    p = n + 2
    parte1 = s[:i] 
    parte2 = s[p:]
    return str(parte1) + str(x) + str(parte2)