def retira_pontuacao(frase):
    """retorna uma frase onde todos os caracteres de pontuação tenham sido substituídos por espaço
    str->str"""
    caracteres = ["-", ",", ":", ";", "."]
    for x in caracteres:
        frasenova = frase.replace(x," ")
        frase = frasenova
    return frase