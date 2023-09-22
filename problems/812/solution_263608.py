def retira_pontuacao(frase):#MAIS CERTO
    if '.' in frase:
        frase=str.replace(frase,'.',' ')
    if ',' in frase:
        frase=str.replace(frase,',',' ')
    if ';' in frase:
        frase=str.replace(frase,';',' ')
    if '...' in frase:
        frase=str.replace(frase,'...',' ')
    if '?' in frase:
        frase=str.replace(frase,'?',' ')
    if '-' in frase:
        frase=str.replace(frase,'-',' ')
    if '!' in frase:
        frase=str.replace(frase,'!',' ')
    return frase