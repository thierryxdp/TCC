def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
	frase = map(lambda x: x.replace(['...','!','?','.',',','-'], ' '), frase)
    
    return nova