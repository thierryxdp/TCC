def retira_pontuacao(frase):
    frase1 = str.replace(frase,'!',' ')
    if '!' in frase:
        return frase1