import re
def retira_pontuacao(frase):
    '''Esta e a funcao que dada uma frase, retorna a frase
    onde todos os caracteres de pontuacao tenham sido 
    substituidos por espaco.
    str->str'''
    frase1=re.sub('[-,:;.]','',frase)
    return frase1