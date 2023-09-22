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
    frase=frase[0::-1]
    return frase