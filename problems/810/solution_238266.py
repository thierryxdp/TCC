def inverte(frase):
    sinal="!,.@?-"
    for remover in sinal:
        frase = frase.replace(remover," ")
        frase = frase[0:-1]
        return frase