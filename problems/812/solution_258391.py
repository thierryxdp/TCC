def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    frase.replace("_"," ")
    frase.replace(","," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    frase.replace("!"," ")
    frase.replace("?"," ")
    frase.replace("."," ")
    return frase(frase.replace("_"," "),frase.replace(","," "),frase.replace(":"," "),frase.replace(";"," "),frase.replace("!"," "),frase.replace("?"," "),frase.replace("."," "))