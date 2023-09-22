def inverte(y):
    """ A função inverte a ordem das palavras da string de entrada. string-->string""" 
    g = retira_pontuacao(x)
    h=str.split(g)
    i=h[::-1]
    return str.lower(str.join(" ",i))