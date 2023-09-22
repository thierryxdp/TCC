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
    return str.lower(frase)
	return list.reverse(frase)