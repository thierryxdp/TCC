def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    if ","  in frase:
        return frase.replace("," , " ")
    elif "!"  in frase:
        return frase.replace("!" , " ")
    elif "?"  in frase:
        return frase.replace("?" , " ")
    elif "-"  in frase:
        return frase.replace("-" , " ")
    elif "."  in frase:
        return frase.replace("." , " ")