def retira_pontuacao(frase):
    lista = list(frase)
    x = map(substitui, lista)
    return x
    resultado = x.join()
    return resultado
    
    
    
def substitui(x):
    pontos = [".", "?", "!", "...", ",", "-", ":", ";"]
    if x in pontos:
        return " "
	else:
        return x