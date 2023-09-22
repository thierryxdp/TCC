def retira_pontuacao(frase3):
    '''função que,dada uma frase, retorne a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço; str -> str'''
    if '.' in frase3:
        frase3=str.replace(frase3,'.',' ')
    if ',' in frase3:
        frase3=str.replace(frase3,',',' ')
    if ';' in frase3:
        frase3=str.replace(frase3,';',' ')
    if '...' in frase3:
        frase3=str.replace(frase3,'...',' ')
    if '?' in frase3:
        frase3=str.replace(frase3,'?',' ')
    if '-' in frase3:
        frase3=str.replace(frase3,'-',' ')
    if '!' in frase3:
        frase3=str.replace(frase3,'!',' ')
    if ':' in frase3:
        frase3=str.replace(frase3,':',' ')
    return frase3    

def inverte(frase3):
       frase3=retira_pontuacao(frase3)
       frase3=str.lower(frase3)
       frase3=list(frase3)
       frase3=frase3[::-1]
    return frase3