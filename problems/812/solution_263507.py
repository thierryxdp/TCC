def retira_pontuacao(frase):
    frase1=''
    if '.' in frase:
        frase1=str.replace(frase,'.',' ')
    if ',' in frase:
        frase1=str.replace(frase,',',' ')
    if ';' in frase:
        frase1=str.replace(frase,';',' ')
    if '...' in frase:
        frase1=str.replace(frase,'...',' ')
    if '?' in frase:
        frase1=str.replace(frase,'?',' ')
    if '-' in frase:
        frase1=str.replace(frase,'-',' ')
    if '!' in frase:
        frase1=str.replace(frase,'!',' ')
        return frase1
        
    else:
        return true