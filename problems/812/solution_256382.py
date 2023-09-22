def retira_pontuacao(texto):
    """Dado uma frase, substitui toda a pontuação dela por espaço."""
    
    texto = frase.replace("?", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace(",", " ")
	#texto = texto.replace(".", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace("_", " ")
    texto = texto.replace("...", " ")
    
    return texto