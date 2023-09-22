def inverte(frase):
    """Inverte uma frase e retorna outra frase sem letras letras maiúscuula e pontuações"""
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("."," ")
    novalista = frase[::-1]
    return str.lower(novalista)