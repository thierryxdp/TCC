def inverte(frase):
    '''funcao que retorna frase sem pontuacao e na ordem inversa'''
    '''str=>str'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    frase=str.lower(frase)
    frase.reverse()
    return frase