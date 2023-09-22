def retira_pontuacao2(frase):
    import string
    p=string.punctuation
    if p in frase:
        frase=str.replace(frase,p,'')
        return frase
    else:
        return frase