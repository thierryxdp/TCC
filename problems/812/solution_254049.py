def retira_pontuacao(frase):
    ''' função que retira a pontuação da frase'''
    if str.replace(frase,'!',' '):
        return frase
    if str.replace(frase,'?',' '):
        return frase