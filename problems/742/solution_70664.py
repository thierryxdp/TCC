def substitui (s,x,i):
    '''função que dada uma string (s), um caractere (x) e um número inteiro (i)
    entre 0 e o comprimento da string retorne uma string igual à informada
    porém com o elemento da posição (i) substituído pelo caractere (x);
    str, str, int -> str'''
    return s[0:i]+x+s[i+1:]