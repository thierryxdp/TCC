def retira_pontuacao(frase):
    '''Dado um frase com entrada, Retorna a mesma frase sem caracteres de pontuação;
    str => str'''
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if '.' in frase:
        frase = frase.replace('.',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    return frase