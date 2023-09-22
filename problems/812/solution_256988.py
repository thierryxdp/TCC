def retira_pontuacao(frase):
    """Retira todas as pontuaçõesda frase, substituindo elas por espaço
       retornando a frase modificada
       str --> str"""
    newFrase = frase
	newFrase = str.replace(newFrase,"!"," ")
	newFrase = str.replace(newFrase,"."," ")
	newFrase = str.replace(newFrase,":"," ")
	newFrase = str.replace(newFrase,"?"," ")
	newFrase = str.replace(newFrase,";"," ")
	newFrase = str.replace(newFrase,","," ")
    return newFrase