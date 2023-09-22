def substitui(s,x,i):
    '''Função que recebe uma string (s), um 
       caractere (x) e um número inteiro (i) 
       entre 0 e o comprimento da string, e retorna 
       uma string igual a s, mas com o elemento da 
       posição i substituído pelo caractere x.
       str, str, int -> str'''
    return s[:i-1] + x + s[i:]