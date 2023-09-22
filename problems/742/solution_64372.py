def substitui(s,x,i):
    '''função que retorna uma string definida trocando um elemento da posição pelo caractere presuposto; string, string, int -> string'''
    return s[0:i] + x + s[i+1:]