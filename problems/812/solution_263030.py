def retira_pontuacao(frase):
    '''Esta e a funcao que dada uma frase, retorna a frase
    onde todos os caracteres de pontuacao tenham sido 
    substituidos por espaco.
    str->str'''
    frase1=frase.replace('-','')
    frase2=frase.replace(',','')
    frase3=frase.replace(':','')
    frase4=frase.replace(';','')
    frase5=frase.replace('.','')
    return frase