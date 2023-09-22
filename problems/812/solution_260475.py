def retira_pontuacao(frase):
    f=frase
    if ',' in frase:
        f=frase.replace(',',' ')
    if '.' in frase:
        f=frase.replace('.',' ')
    if '-' in frase:
        f=frase.replace('-',' ')
    if ';' in frase:
        f=frase.replace(':',' ')
    if ';' in frase:
        f=frase.replace(';',' ')
        return f