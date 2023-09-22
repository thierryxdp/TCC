def retira_pontuacao(frase):
    '''Recebe uma frase como entrada e retorna a mesma sem nenhuma pontuação;
    STR -> STR'''
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    return frase
#
def inverte(frase):
    '''Essa função recebe uma frase como entrada e retorna a mesma sem letras
    maiusculas, sem a pontuação e invertida;
    STR -> STR'''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    return str.join( ,frase)