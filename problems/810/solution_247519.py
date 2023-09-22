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
    '''função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas, e sem a pontuação; str -> str'''
       frase3=retira_pontuacao(frase3)
       frase3=str.lower(frase3)
       frase3=str.split(frase3)
       frase3=frase3[::-1]
       return str.join(' ',frase3)