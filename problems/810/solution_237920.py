def inverte (frase):
    """Recebe uma frase e retorna ela sem pontuação, sem 
    letras maiúsculas e com a ordem das palavras invertida.
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
    x = str.split(x, " ")
    x = list.reverse(x)
    return str.lower(str.join (" ", x))