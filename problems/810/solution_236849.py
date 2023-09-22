def inverte(frase):
    '''retorna a frase dada de trás pra frente, sem letras maisculas e sem pontuação'''
    for char in "-,.?!:;":
        frase = frase.replace(char, " ")
        frase.split()
    list = str.split(frase)
    list.reverse()
    frase = str.join(" ", list)
    return frase