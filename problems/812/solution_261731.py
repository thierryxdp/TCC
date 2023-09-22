def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase com espaço no lugar dos caracteres de pontuação
    str -> str"""
    x = frase
    if "-" in x:
        return str.replace(x, "-", " ")
    if "," in x:
        return str.replace(x, ",", " ")
    if ":" in x:
        return str.replace(x, ":", " ")
    if ";" in x: 
        return str.replace(x, ";", " ")
    if "." in x:
        return str.replace(x, ".", " ")
    if "!" in x:
        return str.replace(x, "!", " ")
    if "?" in x:
        return str.replace(x, "?", " ")