def uppCons(frase):
    """
    str->str
    :param frase: Recebe uma frase
    :param return: Retorna um frase com as consoantes em maiusculo
    """
    i = 0
    string = ""
    while i < len(frase):
        if frase[i] in "AEIOUaeiouáéãõíúÁÉÃÍÕÚ":
            string = string + frase[i]
        else:
            string = string +frase[i].upper()
        i = i + 1
    return string