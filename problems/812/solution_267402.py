def retira_pontuacao(frase):
    lista = list(frase)
    x = map(substitui, lista)
    resultado = x.join()
    return resultado
    
    
    
def substitui(x):
    pontos = [".", "?", "!", "...", ",", "-", ":", ";"]
    if x in pontos:
        return " "
	else:
        return x