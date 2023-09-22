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
    frase = retira_pontuacao(frase)
    frase = str.lower(frase
    frase = frase.split(" ")
	return list.reverse(frase)