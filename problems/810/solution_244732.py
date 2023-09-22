def inverte(frase):
    '''retorne uma outra frase na ordem inversa'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase

frase.reverse(frase)
return frase