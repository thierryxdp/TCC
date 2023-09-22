def inverte (frase):
    '''função que dada uma frase retorna uma outra frase com as mesmas palavras
    da frase original na ordem inversa, sem letras maiúsculas e sem pontuação;
    str -> str'''
    lista = str.split(str.lower(frase))[::-1]
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
    def inverte (frase):
    return str.join(' ',lista)