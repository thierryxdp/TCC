def retira_pontuacao(frase):
    '''ao receber uma frase, retorna a mesma frase,
    porém sem pontuação.
    str -> str'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('...',' ')
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = str.split(frase, ' ')
    return frase[-1]