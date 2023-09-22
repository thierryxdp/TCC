def invertida(frase):
    frase=str.lower(frase)
    pontuação=['...','.','!','?','-',',',':',';']
    for x in pontuação:
        frase=frase.replace(x,' ')
    frase=(str.split(frase)[::-1])
    frase=' '.join(frase)
    return frase