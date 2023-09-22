def retira_pontuacao(frase):
    f=frase
    if ',' in frase:
        f=frase.replace(',',' ')
    elif '.' in frase:
        f=frase.replace('.',' ')
    elif '-' in frase:
        f=frase.replace('-',' ')
    elif ';' in frase:
        f=frase.replace(':',' ')
    elif ';' in frase:
        f=frase.replace(';',' ')
    return f