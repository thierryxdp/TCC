def substitui(s,x,i):
    '''função que retorna uma string igual a s, exceto que o elemento da
    posição i é substituido pelo caractere x
    str, int, int -> str'''
    return s[:i] + str(x) + s[i+1:]