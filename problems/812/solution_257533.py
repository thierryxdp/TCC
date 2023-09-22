def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
	frase = str(map(lambda x: x.replace(['...','!','?','.',',','-'], ' '), frase))
    
    return frase