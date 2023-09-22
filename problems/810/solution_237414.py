def inverte(frase):
    """
    str->str
    :param frase: Recebe uma frase
    :return: Esta função pega uma frase e retorna esta mesma frase ao contrário
    """
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ",lista)
    return frase