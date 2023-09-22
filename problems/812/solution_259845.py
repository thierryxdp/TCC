def retira_pontuacao(frase):
    '''Retorna a frase que todos os caracteres de pontuação tenham sido substituídos por espaço'''
    #str->str
    if "." in frase:
        frase = frase.replace(".", " ")
        elif "," in frase:
        frase = frase.replace(",", " ")
        elif ";" in frase:
        frase = frase.replace(";", " ")
        elif "!" in frase:
        frase = frase.replace("!", " ")
        elif "?" in frase:
        frase = frase.replace("?", " ")
        elif ":" in frase:
        frase = frase.replace(":", " ")
        elif "-" in frase:
        frase = frase.replace("-", " ")
    return frase