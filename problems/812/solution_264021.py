def retira_pontuacao(frase):
    '''Função que,dada uma frase, retorne a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
    str -> str'''
    frase = str.replace(frase,';:.,/!?',' ')
return frase