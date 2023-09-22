def retira_pontuacao(frase):
    """retorna frase substituindo os caracteres de pontuação por espaço
       str->str"""
    frase= frase.replace("!"," ")
    frase= frase.replace(":"," ")
    frase= frase.replace(";"," ")
    frase= frase.replace("."," ")
    frase= frase.replace("-"," ")
    frase= frase.replace(","," ")
    frase= frase.replace("?"," ")
    return frase