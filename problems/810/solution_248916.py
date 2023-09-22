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
    '''funcao''''
    frase=retira_pontuacao(frase)
    palavras=frase.split(' ')
    palavras.remove('')
    palavras.reverse()
    return palavras