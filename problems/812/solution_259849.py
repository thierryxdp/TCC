def retira_pontuacao(frase):
    frase1 = 0
    frase2 = 0
    frase3 = 0
    frase4 = 0
    frase5 = 0
    frase6 = 0
    frase7 = 0
    frase8 = 0
    frase9 = 0
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