def inverte (frase):
    '''funcao que retorne a frase em ordem inversa'''
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(" ", lista)
    return frase