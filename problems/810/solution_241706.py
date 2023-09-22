def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase transformando as
    pontuações em espaços.
    str -> str'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('...',' ')
    return frase

def inverte(frase):
    '''Dada uma frase, inverte suas palavras e retorna esta
    frase invertida.
    str -> str'''
    frase = str.lower(frase)
    frase = retira_pontuacao(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase