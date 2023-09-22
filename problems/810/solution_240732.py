def inverte(frase):
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
    if ' ' in frase:
        frase.lower = frase.split()
        frase.lower = farse
        return ' '.join(reversed(frase))