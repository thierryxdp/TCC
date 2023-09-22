def retira(frase):
    b="!@#$%&*().,:-;"
    for i in range(len(b)):
        frase=frase.replace(b[i]," ")
    return frase