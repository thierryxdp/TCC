def conta_palavras(frase):
    if frase[-1] == ' ':
        frase= frase[:-2]
        frase=frase.split(' ')
        return len(frase)
    else:
        frase=frase.split(' ')
        return len(frase)