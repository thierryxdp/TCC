def inverte(frase):
    """
    Retorna uma frase sem letras maiusculas, sem pontuacao e na ordem 
    inversa da que foi escrita inicialmente;
    str -> str
    """
    def retira_pontuacao(frase):
    frase = frase.replace("."," ") 
    frase = frase.replace("..."," ")
    frase = frase.replace(","," ")
    frase = frase.replace("?"," ") 
    frase = frase.replace("!"," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    return frase