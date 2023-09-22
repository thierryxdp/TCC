def retira_pontuacao(frase):
    if ',' in frase:
        frase.replace(',','')
    elif '.' in frase:
        frase.replace('.','')
    elif '?' in frase:
        frase.replace('?',' ')
    return frase