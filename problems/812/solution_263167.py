def retira_pontuacao(frase):
    """Substitui os caracteres de pontuação por espaços. (str->str)"""
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
        
    return frase