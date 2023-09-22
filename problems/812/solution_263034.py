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
    e1='-'
    e2=','
    e3=':'
    e4=';'
    e5='.'
    if e1 and e2 and e3 and e4 and e5 in frase:
        return frase1+frase2+frase3+frase4