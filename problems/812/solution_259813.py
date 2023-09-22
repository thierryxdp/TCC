def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
    if '.' in frase:
        frase=frase.replace('.', ' ')
    if '?' in frase:
        frase=frase.replace('?', ' ')
    if '-' in frase:
        frase=frase.replace('-', ' ')
    if ':' in frase:
        frase=frase.replace(':', ' ')
    if ',' in frase:
        frase=frase.replace(',', ' ')
    if ';' in frase:
        frase=frase.replace(';', ' ')
	if '!' in frase:
        frase=frase.replace('!', ' ')
    return frase