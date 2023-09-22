def inverte(frase):
    '''Funcao que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase na ordem inversa, sem letras maiusculas e pontuação.'''
    ''' str -> str'''

    
    lista = str.split(frase, " ")
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(" ", lista)
    frase = str.lower(frase)
    for char in [".", "...","!","?",",",":",";","-"]:
        frase = str.replace(frase, char, "")
    return frase