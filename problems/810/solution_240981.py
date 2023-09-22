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
    val = frase.split()
    lav = list(reversed(val))
    StringFinal = (' '.join(lav))
    return StringFinal.lower()