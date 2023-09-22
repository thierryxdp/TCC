def retira_pontuacao (frase):
    frase=frase.replace("-"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase

def inverte (frase):
    """dada uma frase, retorna outra contendo as mesmas palavras na ordem inversa, sem pontuacao e letras maiusculas."""
    frase=retira_pontuacao(frase)
    frase=frase.lower()
    teste=frase.split(" ")
    teste=teste[::-1]
    frase=str.join(" ",teste)
    return frase