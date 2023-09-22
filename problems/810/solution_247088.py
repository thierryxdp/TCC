def inverte(frase):
    ''' '''
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

    frase1=frase.split(' ')
    list.reverse(frase1)
    return str.lstrip(str.lower(str.join(' ',frase1)),' ')