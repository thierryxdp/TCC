def inverte (frase):
    '''função que dada uma frase retorna uma outra frase com as mesmas palavras
    da frase original na ordem inversa, sem letras maiúsculas e sem pontuação;
    str -> str'''
        if '.' in frase:
        frase = frase.replace('.',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    return str.join(' ',str.split(str.lower(frase)))[::-1]