def substitui(s1,x,i):
    '''Função que, dados uma string (s1), um caractere (x) e um número inteiro (i) entre 0 e o comprimento da string, retorna uma string igual a (s1), porém com o elemento da posição (i) trocado pelo caractere (x); str, int, int -> str.'''
    comprimento = len(s1)
    if (i > 0 and i < comprimento):
        s1.replace(s1[i], x) = s2
    return s2