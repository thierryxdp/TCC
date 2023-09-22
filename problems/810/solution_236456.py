def substituir(frase12):
    ''' '''
    if '.' in frase12:
        frase0 = frase12.replace('.',' ')
    if '-' in frase12:
        frase0 = frase12.replace('-',' ')
    if ',' in frase12:
        frase0 = frase12.replace(',',' ')
    if ':' in frase12:
        frase0 = frase12.replace(':',' ')
    if ';' in frase12:
        frase0 = frase12.replace(';',' ')
    if '?' in frase12:
        frase0 = frase12.replace('?',' ')
    if '!' in frase12:
        frase0 = frase12.replace('!',' ')
    return frase0
def inverte(frase):
    ''' essa funcao retorna a frase dada na entrada invertida '''
    frase1 = substituir(frase)
    semMaiuscula = str.lower(frase1)
    listaDaFrase = str.split(semMaiuscula)
    listainvertida = (listaDaFrase[::-1])
    final = str.join(' ',listainvertida)
    return final