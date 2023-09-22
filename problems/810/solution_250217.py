def retira_pontuacao(frase):
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if ':' in frase:
        frase = frase.replace(':', ' ')
    if '.' in frase:
        frase = frase.replace('.', ' ')
    if '!' in frase:
        frase = frase.replace('!', ' ')
    if '?' in frase:
        frase = frase.replace('?', ' ')
    return frase



def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase)
    return frase[::-1]