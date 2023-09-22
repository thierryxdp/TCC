def retira_pontuacao (frase):
    """Retira os caracteres de pontuação da frase, e os 
    substitui por espaço.
    str -> str"""
    x = frase
    if str.count(x, ",") > 0:
        x=str.replace(x, ",", " ")
    if str.count(x, ";") > 0:
        x=str.replace(x, ";", " ")
    if str.count(x, ":") > 0:
        x=str.replace(x, ":", " ")
    if str.count(x, "-") > 0:
        x=str.replace(x, "-", " ")
    if str.count(x, ".") > 0:
        x=str.replace(x, ".", " ")
    if str.count(x, "!") > 0:
        x=str.replace(x, "!", " ")
    if str.count(x, "?") > 0:
        x=str.replace(x, "?", " ")
    return x