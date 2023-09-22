def inverte(frase):
    '''Funcao que dada uma frase, retorna uma outra frase que contem as
    mesmas palavras da frase de entrada na ordem inversa
    str -> str'''
    frase = str.replace(frase,"-", " ")
    frase = str.replace(frase,",", " ")
    frase = str.replace(frase,":", " ")
    frase = str.replace(frase,";", " ")
    frase = str.replace(frase,".", " ")
    frase = str.replace(frase,"!", " ")
    frase = str.replace(frase,"?", " ")
    lista = str.split(frase)
    inverso = lista[::-1]
    resultado = str.join(" ",inverso)
    return resultado