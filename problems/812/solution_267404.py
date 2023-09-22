def retira_pontuacao(frase):
    x = map(substitui, frase)
    return x
    
    
    
def substitui(x):
    pontos = [".", "?", "!", "...", ",", "-", ":", ";"]
    if x in pontos:
        return " "
	else:
        return x