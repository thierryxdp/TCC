def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    return (frase.replace("_"," ") and frase.replace(","," ") and frase.replace(":"," ") and frase.replace(";"," "),frase.replace("!"," ") and frase.replace("?"," ") and frase.replace("."," "))