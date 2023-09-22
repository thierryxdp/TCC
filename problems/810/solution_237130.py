def inverte (frase) :
    """Funcao que dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa"""
    frase = str.replace(frase, '-', " ")
    frase = str.replace(frase, ',', " ")
    frase = str.replace(frase, '.', " ")
    frase = str.replace(frase, ':', " ")
    frase = str.replace(frase, ';', " ")
    frase = str.replace(frase, '!', " ")
    frase = str.replace(frase, '?', " ")
    frase = str.replace(frase, '...', " ")
    frase = str.replace(frase, '#', " ")
    frase = str.replace(frase, '()', " ")
    frase = str.replace(frase, '[]', " ")
    frase = str.replace(frase, '"', " ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase