def retira_pontuacao(frase):
    ''' retorna a frase com todos os caracteres de pontuacao
    substituidos por espaço; str->str'''
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if ':' in frase:
        frase= frase.replace(':',' ')
    if ';' in frase:
        frase= frase.replace(';',' ')
    if '.' in frase:
        frase= frase.replace('.',' ')
    if '?' in frase:
        frase= frase.replace('?',' ')
    if '!' in frase:
        frase= frase.replace('!',' ')
    return frase
def inverte(frase):
    '''Retorna uma outra frase que tem as mesmas palavras
    da frase de entrada,porem na ordem inversa;str->str'''
    frase1=retira_pontuacao(frase).split()
    list.reverse(frase1)
    return str.lstrip(str.lower(str.join(' ',frase1)),' ')