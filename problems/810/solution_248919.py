def retira_pontuacao(frase):
    '''Funcao que dada uma frase retorna uma frase inde todos os caracteres de pontuacao tenham sido substituids
'''
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    return frase

def inverte(frase):
    '''uhggu''''
    frase=retira_pontuacao(frase)
    palavras_sujo=frase.split(' ')
    palavras = []
    for palavra in palavras_sujo:
        if palavra != '':
          palavras.append(palavra)
    palavras.reverse()
    return palavras.join(' ')