def substitui(s,x,i):
    '''esta função recebe uma stirng s, um caractere x e um número inteiro i entre zero e o comprimento da string e retorna uma string igual a s, exceto que o elemento da posição i é substituido pelo caractere x
    string, int, int -> string'''
    return s[:i]+'x'[i+1:]