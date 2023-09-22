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

def inverte(frase):
    """Inverte a frase, sem pontuação, contendo as mesmas palavras
       str --> str"""
    str.split(frase)
    str.join(" ",frase)
    return retira_pontuacao(frase[:-1])