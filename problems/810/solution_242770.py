def inverte(frase):
    frase=str.lower(frase)
    pontuacao=['...','.','!','?','-',',',':',';']
    for x in pontuacao:
        frase=frase.replace(x,' ')
    frase=(str.split(frase)[::-1])
    frase=' '.join(frase)
    return frase