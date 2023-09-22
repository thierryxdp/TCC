def retira_pontuacao(frase):
    """Retorna a frase com os caracteres de pontuação substituidos por espaço;
    str->str"""
    frase=frase.replace("."," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    return frase