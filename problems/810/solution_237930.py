def inverte (frase):
    """Recebe uma frase e retorna ela sem pontuação, sem 
    letras maiúsculas e com a ordem das palavras invertida.
    str -> str"""
    frase2 = frase [-1:]
    x = str.lower(frase2)
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
    return str.join(" ", str.split(x, " "))