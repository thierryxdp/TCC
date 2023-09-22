def retira_pontuacao(frase):
    import string
    p=string.punctuation
    if p in frase:
        frase=str.replace(frase,p,'')
        return frase
    else:
        return str.replace(frase,p,'')