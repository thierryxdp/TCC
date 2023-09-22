def inverte (frase):
    """Recebe uma frase e retorna ela sem pontuação, sem 
    letras maiúsculas e com a ordem das palavras invertida.
    str -> str"""
    x = str.lower(frase)
    if str.count(x, ",") > 0:
        x=str.replace(x, ",", "")
    if str.count(x, ";") > 0:
        x=str.replace(x, ";", " ")
    if str.count(x, ":") > 0:
        x=str.replace(x, ":", " ")
    if str.count(x, "-") > 0:
        x=str.replace(x, "-", " ")
    if str.count(x, ".") > 0:
        x=str.replace(x, ".", "")
    if str.count(x, "!") > 0:
        x=str.replace(x, "!", "")
    if str.count(x, "?") > 0:
        x=str.replace(x, "?", "")
    return str.join(" ", str.split(x," ")[::-1])