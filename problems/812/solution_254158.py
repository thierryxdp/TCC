def retira_pontuacao(frase):
    if '.' in frase:
        frase = frase.replace('.',' ')
    
    elif '!' in frase:
        frase = frase.replace('!',' ')

    elif '?' in frase:
        frase = frase.replace('?',' ')

    elif '...' in frase:
        frase = frase.replace('...',' ')

    elif '-' in frase:
        frase = frase.replace('-',' ')

    elif ',' in frase:
        frase = frase.replace(',',' ')

    elif ':' in frase:
        frase = frase.replace(':',' ')

    elif ';' in frase:
        frase = frase.replace(';',' ')
    
    return frase