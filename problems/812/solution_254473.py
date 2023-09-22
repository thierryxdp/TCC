import re
def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos caracteres de pontuação tenham sido substituidos por espaço
    str -> str'''
    s = frase
    out = re.sub(r'[^\w\s]','',s)
    return out