def retira_pontuacao(frase):
    """Retira todas as pontuaçõesda frase, substituindo elas por espaço
       retornando a frase modificada
       str --> str"""
	frase = str.replace(frase,"!"," ")
	frase = str.replace(frase,"."," ")
	frase = str.replace(frase,":"," ")
	frase = str.replace(frase,"?"," ")
	frase = str.replace(frase,";"," ")
	frase = str.replace(frase,","," ")
    frase = str.replace(frase,"-"," ")
	return frase

def inverte(frase):
    """Inverte a frase, sem pontuação, contendo as mesmas palavras
       str --> str"""
    frase = str.lower(frase)
    frase = str.split(frase," ")
    frase = str.join(" ",frase)
    frase = retira_pontuacao(frase)
    frase = str.reverse()
    return frase