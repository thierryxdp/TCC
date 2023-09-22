def retira_pontuacao(frase):
    import string
    p=string.punctuation
    for c in p:
        frase=frase.replace(c," ")
    return frase


def inverte(frase):
    retira_pontuacao(frase)
    str.split(frase)
    list.reverse(frase)
    str.join(' ',frase)
    return frase