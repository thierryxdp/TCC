def retira_pontuacao(frase):
    """ Retorna a frase onde todos os caracteres de pontuaçao tenham sido substituidos por espaço;
    string->string """
    if ";" in frase:
        frase=frase.replace(";"," ")
    if "-" in frase:
         frase=frase.replace("-"," ")
    if "," in frase:
        frase=frase.replace(","," ")
    if ":" in frase:
        frase=frase.replace(":"," ")
    if "." in frase:
        frase=frase.replace("."," ")
    if "!" in frase:
        frase=frase.replace("!"," ")
    if "?" in frase:
        frase=frase.replace("?"," ")
    return frase