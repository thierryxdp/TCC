def retira_pontuacao(frase):
    '''função que,dada uma frase, retorne a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço; str -> str'''
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
    if ':' in frase:
        frase=str.replace(frase,':',' ')
    return frase