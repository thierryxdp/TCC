def inverte (frase):
    '''Dada uma frase retorna uma outra que contenha as mesmas
    palavras da frase de entrada na ordem inversa'''
    lista = str.split (frase)
    list.reverse(lista)
    frase = str.join(" ",lista)
    return frase