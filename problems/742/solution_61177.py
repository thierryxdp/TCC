def substitui(s,x,i):
    '''Funcao que retorna uma string igual a s, exceto que o elemento da
    posicao i e substituido pelo caractere x, dados s, x e i
    string, int, int -> string'''
    s = s[:i] + x + s[i + 1:]
    return s