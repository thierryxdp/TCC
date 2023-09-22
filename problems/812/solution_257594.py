def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    if ","  in frase:
        frase = frase.replace("," , " ")
    if "!"  in frase:
        frase = frase.replace("!" , " ")
    if "?"  in frase:
        frase = frase.replace("?" , " ")
    if "-"  in frase:
        frase = frase.replace("-" , " ")
    if "."  in frase:
        frase = frase.replace("." , " ")
    return frase