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