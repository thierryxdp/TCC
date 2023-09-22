def substitui(s,x,i):
    '''
       Função que recebe uma string (s), um caractere (x)
       e um numero inteiro (i) entre 0 e o comprimento de s,
       e retorna uma string igual a s, exceto que o elemento
       na posição i sera substituído por x.
       string, int, int -> string
    '''
    sub = s[0:i]+x+s[i+1:]
    return sub