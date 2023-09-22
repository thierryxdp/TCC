def retira_pontuacao(frase): 
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
        
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    lista = frase.split()
    atsil = list(reversed(lista))
    stringFinal = (' '.join(lav))
    return stringFinal.lower()