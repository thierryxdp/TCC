def retira_pontuacao(frase):#MAIS CERTO
    frase1=''
    if '.' in frase:
        frase1=str.replace(frase,'.',' ')
    if ',' in frase:
        frase1=str.replace(frase1,',',' ')
    if ';' in frase:
        frase1=str.replace(frase1,';',' ')
    if '...' in frase:
        frase1=str.replace(frase,'...',' ')
    if '?' in frase:
        frase1=str.replace(frase,'?',' ')
    if '-' in frase:
        frase1=str.replace(frase,'-',' ')
    if '!' in frase:
        frase1=str.replace(frase,'!',' ')
    return frase1