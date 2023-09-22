def retira_pontuacao(frase):
    """retorna uma frase onde todos os caracteres de pontuação tenham sido substituídos por espaço
    str->str"""
    caracteres = ["-", ",", ":", ";", "."]
    for x in caracteres:
        frase.replace(x," ")
    return frase