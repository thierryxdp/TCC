def retirar(frase):
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in ['-',',',':',';','.','!','?']:
            frase[i] = ' '
    return frase

def retira_pontuacao(frase):
    frase = list(map(retirar,frase))
    return frase