def substituir(frase):
    ''' '''
    if '.' in frase:
        frase = frase.replace('.',' ')
        if '_' in frase:
            frase = frase.replace('_',' ')
        if ',' in frase:
            frase = frase.replace(',',' ')
        if ':' in frase:
            frase = frase.replace(':',' ')
        if ';' in frase:
            frase = frase.replace(';',' ')
        if '?' in frase:
            frase = frase.replace('?',' ')
        if '!' in frase:
            frase = frase.replace('!',' ')
    return frase
def inverte(frase):
    ''' essa funcao retorna a frase dada na entrada invertida '''
    frase1 = substituir(frase)
    semMaiuscula = str.lower(frase1)
    listaDaFrase = str.split(semMaiuscula)
    listainvertida = (listaDaFrase[::-1])
    final = str.join(' ',listainvertida)
    return final