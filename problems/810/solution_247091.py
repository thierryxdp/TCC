def inverte(frase):
    ''' retorna a frase com todos os caracteres de pontuacao
    substituidos por espaço; str->str'''
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
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    return frase