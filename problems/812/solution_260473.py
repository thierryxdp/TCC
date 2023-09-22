def retira_pontuacao(frase):
    frase=frase
    if ',' in frase:
        frase=frase.replace(',',' ')
    if '.' in frase:
        frase=frase.replace('.',' ')
    if '-' in frase:
        frase=frase.replace('-',' ')
    if ';' in frase:
        frase=frase.replace(':',' ')
    if ';' in frase:
        frase=frase.replace(';',' ')