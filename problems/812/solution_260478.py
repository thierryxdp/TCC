def retira_pontuacao(frase):
    f=()
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