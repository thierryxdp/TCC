def substituir(frase):
    ''' '''
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '-' in frase:
        frase = frase.replace('-',' ')
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
# Número 5

def inverte(frase):
    ''' essa funcao inverte uma frase dada como entrada e retira sua pontuacao '''
    frase1 = substituir(frase)
    semMaiuscula = str.lower(frase1)
    listaDaFrase = str.split(semMaiuscula)
    listainvertida = (listaDaFrase[::-1])
    final = str.join(' ',listainvertida)
    return final