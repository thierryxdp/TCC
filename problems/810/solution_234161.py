def retira_pontuacao(frase):

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
    
    return frase
    


    
def inverte(frase):

    frase = retira_pontuacao(frase)
    frase = str.split(frase,)
    frase = list(frase[::-1])
    frase = str.join('',frase)
    frase = str.lower(frase)



    return frase