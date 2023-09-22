def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
	frase = str(map(lambda frase: frase.replace(['...','!','?','.',',','-'], ' '), frase))
    
    return frase