def substitui(s,x,i):
    """ retorna uma string mudando o caractere na posição i 
    pelo caractere x."""
    i = s[i]
    s[i] = x
    return str(x) - i + x