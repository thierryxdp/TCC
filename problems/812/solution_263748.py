def retira_pontuacao(frase):
    '''
    função que dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço
    str -> str
    '''
    frase1 = str.replace(frase,'...',' ')
    frase2 = str.replace(frase1,'.',' ')
    frase3 = str.replace(frase2,'!',' ')
    frase4 = str.replace(frase3,'?',' ')
    frase5 = str.replace(frase4,'-',' ')
    frase6 = str.replace(frase5,',',' ')
    frase7 = str.replace(frase6,':',' ')
    frase8 = str.replace(frase7,';',' ')
    return frase8