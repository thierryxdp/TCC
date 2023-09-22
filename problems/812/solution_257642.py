def retira_pontuacao(frase):
    frase1 = str.replace(frase,'!',' ')
    frase2 = str.replace(frase,'.',' ')
    frase3 = str.replace(frase,'-',' ')
    frase4 = str.replace(frase,',',' ')
    frase5 = str.replace(frase,':',' ')
    frase6 = str.replace(frase,'?',' ')
    frase7 = str.replace(frase,';',' ')
    if '!' in frase:
        return frase1
    if '.' in frase:
        return frase2
    if  '-' in frase:
        return frase3
    if ',' in frase:
        return frase4
    if ':' in frase:
        return frase5
    if '?' in frase:
        return frase6
    if ';' in frase:
        return frase7