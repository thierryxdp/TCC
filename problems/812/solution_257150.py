def retira_pontuacao(frase):
    """Troca pontuações por espaços numa frase. str->str"""
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("."," ")
    return frase