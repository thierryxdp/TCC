def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
	frase1=frase
    frase1=frase.replace('.', ' ')
    frase1=frase1.replace('?', ' ')
    frase1=frase1.replace('-', ' ')
    frase1=frase1.replace(':', ' ')
    frase1=frase1.replace(',', ' ')
    frase1=frase1.replace(';', ' ')
	frase1=frase1.replace('!', ' ')
    	return frase1