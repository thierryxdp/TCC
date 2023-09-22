def retira_pontuacao(frase):
    ''' funcao que dada uma frase retorna outra frase onde toda a pontuacao foi subsituida por um espaco ('')'''
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase=frase.replace(',',' ')
    if ':' in frase:
        frase=frase.replace(':',' ')
    if ';' in frase:
        frase=frase.replace(';',' ')
    if '.' in frase:
        frase=frase.replace('.',' ')
    if '!' in frase:
        frase=frase.replace('!',' ')
    if '?' in frase:
        frase=frase.replace('?',' ')
    return frase


def inverte(frase):
    '''funcao que dada uma frase retorna a frase com a ordem invertida'''
    frase=retira_pontuacao(frase)
    frase= frase[::-1]
    return frase