def inverte(frases):
    '''função que retorna a frase na ordem inversa sem letras maiúsculas e pontuação; str => str'''
    frases = frases.replace("."," ")
    frases = frases.replace("/"," ")
    frases = frases.replace(";"," ")
    frases = frases.replace(","," ")
    frases = frases.replace(":"," ")
    frases = frases.replace("-"," ")
    frases = frases.replace("?"," ")
    frases = frases.replace("!"," ")
    frases = str.lower(frases)
    palavra = frases.split()
    palavra = list(reversed(palavra))
    return (" ".join(palavra))