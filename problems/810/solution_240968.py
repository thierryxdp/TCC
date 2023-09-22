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
    atsil = list(lista(range(0, -1, -1))
    stringFinal = (' '.join(atsil))
    return stringFinal.lower()