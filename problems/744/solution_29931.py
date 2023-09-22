def hashtag(str1):
    """Função que recebe uma string e insere o caractere
    "#" no ínicio, no meio e no fim dela.
    str->str
    """
    return "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"