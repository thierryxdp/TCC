def retira_pontuacao(frase):
    import string
    p=string.punctuation
    for c in p:
        frase=frase.replace(c," ")
    return frase


def inverte(frase):
    retira_pontuacao(frase)
    list(frase)
    i=1
    n=[]
    while i<len(frase)
    for i in frase:
        n.append(frase[-i])
    i=i+1
    return str(n)