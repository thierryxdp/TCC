def inverte(frase):
    '''funccao que dada uma frase retorna a frase invertida.'''
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase