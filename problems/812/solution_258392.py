def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    return frase(frase.replace("_"," "),frase.replace(","," "),frase.replace(":"," "),frase.replace(";"," "),frase.replace("!"," "),frase.replace("?"," "),frase.replace("."," "))