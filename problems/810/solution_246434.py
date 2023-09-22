def retira_pontuacao(frase):
    """Recebe uma frase e a retorna sem pontuacao; str-> str."""
    frase= frase.replace("."," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    return frase
def inverte(frase):
    """Recebe uma frase e retorna a mesma frase na ordem inversa e sem pontuacao; str->str."""
	frase=retira_pontuacao(frase)
    list.sort(frase)
    return frase