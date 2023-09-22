def retira_pontuacao(frase):
    '''dsadadas'''
    if '.' in frase:
        frase=frase.replace('.', ' ')
    if '?' in frase:
        frase=frase.replace('?', ' ')
    if '-' in frase:
        frase=frase.replace('-', ' ')
    if ':' in frase:
        frase=frase.replace(':', ' ')
    if ';' in frase:
        frase=frase.replace(';', ' ')
    if '!' in frase:
        frase=frase.replace('!', ' ')
	if ',' in frase:
        frase=frase.replace(',', ' ')
    return frase