def inverte(frase):
    '''
       Funcao que recebe uma frase e
       retorna seu inverso, sem pontuacao
       e sem letras maiusculas.
       str -> str
    '''
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

    FRASE = frase.split(' ')
    range_FRASE = len(FRASE)+1
    Frase = FRASE[-1:(range_FRASE):-]
    frase_inversa = str.join(' ',Frase)

    return str.lower(frase_inversa)