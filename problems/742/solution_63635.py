def substitui(s,x,i):
    '''retorna uma string igual a s, exceto que o elemento da
    posição i é substituído pelo caractere x; 
    str, str, int -> str'''
    return s[:i]+x+s[(i+1):]