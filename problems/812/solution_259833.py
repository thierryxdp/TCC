def retira_pontuacao(frase):
    if '-' in frase:
        frase.replace('-',' ')
    if ',' in frase:
        frase.replace(',',' ')
    if ':' in frase:
        frase.replace(':',' ')
    if ';' in frase:
        frase.replace(';',' ')
    if '.' in frase:
        frase.replace('.',' ')
    if '...' in frase:
        frase.replace('...',' ')
    if '!' in frase:
        frase.replace('!',' ')
    if '?' in frase:
        frase.replace('?',' ')
    return frase