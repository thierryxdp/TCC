def inverte(frase):
    ''' função que dada uma frase, retorna a mesma frase de entrada na ordem inversa sem pontuações.
    str -> str
    '''
    frase=frase.replace("."," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=frase.lower()
    frase=frase.reverse()
    return frase