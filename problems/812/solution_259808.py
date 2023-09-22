def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
	frase1=frase
    if '.' in frase:
        frase1=frase.replace('.', ' ')
    if '?' in frase:
        frase1=frase.replace('?', ' ')
    if '-' in frase:
        frase1=frase.replace('-', ' ')
    if ':' in frase:
        frase1=frase.replace(':', ' ')
    if ',' in frase:
        frase1=frase.replace(',', ' ')
    if ';' in frase:
        frase1=frase.replace(';', ' ')
	if '!' in frase:
        frase1=frase.replace('!', ' ')
    	return frase