def retira_pontuacao(frase):
    if '-' in frase:
        frase1 = frase.replace('-',' ')
    if ',' in frase:
        frase2 = frase.replace(',',' ')
    if ':' in frase:
        frase3 = frase.replace(':',' ')
    if ';' in frase:
        frase4 = frase.replace(';',' ')
    if '.' in frase:
        frase5 = frase.replace('.',' ')
    if '...' in frase:
        frase6 = frase.replace('...',' ')
    if '!' in frase:
        frase7 = frase.replace('!',' ')
    if '?' in frase:
        frase8 = frase.replace('?',' ')
        
    return frase1+frase2