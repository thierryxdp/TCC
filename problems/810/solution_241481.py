def retira_pontuacao(frase):
    '''ao receber uma frase, retorna a mesma frase,
    porém sem pontuação.
    str -> str'''
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    return frase

def inverte(frase):
    '''ao receber uma frase, remove toda a pontuação
    e inverte as palavras.
    str -> str'''
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase = frase[-1::-1]
    frase = ' '.join(frase)
    return frase