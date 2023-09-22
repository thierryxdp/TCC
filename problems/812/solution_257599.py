def retira(frase):
    sinal = "!,.@?-"
    for remover in sinal:
        frase = frase.replace(remover," ")
    return frase