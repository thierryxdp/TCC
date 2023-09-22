def retira_pontuacao(frase):   
    if ('.' in frase):
        frase = frase.replace('.', '')
    if ('-' in frase):
        frase = frase.replace('-', '')
    if (',' in frase):
        frase = frase.replace(',','')
    if (':' in frase):
        frase = frase.replace(':', '')
    if (';' in frase):
        frase = frase.replace(';', '')
    if ('?' in frase):
        frase = frase.replace('?', '')
    if ('!' in frase):
        frase = frase.replace('!', '')
    return frase

def inverte(frase):
    frase = frase.lower()
    return str(type(frase))
    frase = retira_pontuacao(frase)
    #frase = frase.split()
	return frase