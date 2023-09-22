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
    frase = frase.split(' ')
    frase = frase[-1] + frase[-2] + frase[-3] + frase[-4] + frase[-5] + frase[-6] + frase[-7] + frase[-8]
    return frase