def inverte(x):
    """ A função inverte a ordem das palavras da string de entrada. string-->string""" 
    h=str.split(x)
    i=h[::-1]
    return str.lower(str.join(" ",i))