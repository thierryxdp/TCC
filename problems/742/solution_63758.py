def substitui(s,x,i):
    """ Retorna a string (s) modificando o elemento da posição (i)
    pelo caractere (x).
    str, int, int -> str"""
    return s[0:i] + str(x) + s[i+1:]