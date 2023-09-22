def retira_pontuacao (frase):
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
    return x