def inverte(frase):
    """
    str->str
    :param frase: Recebe uma frase
    :return: Esta função pega uma frase e retorna esta mesma frase ao contrário
    """
    for char in ".!?-:;,":
    string = string.replace(char, " ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ",lista)
    return frase