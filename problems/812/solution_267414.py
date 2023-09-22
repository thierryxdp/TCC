def retira_pontuacao(frase):
    '''função que dada uma frase substitui todos os caracteres de pontuação por espaços. str -> str'''
    if '.' in frase:
        frase = frase.replace('.',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')
    if '-' in frase:
        frase = frase.replace('-',' ')
    return (frase)