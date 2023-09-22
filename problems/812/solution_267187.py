def retira_pontuacao(frase):
    import string
    y=string.punctuation
    for x in y:
        frase = frase.replace(x,'')
    return(frase)