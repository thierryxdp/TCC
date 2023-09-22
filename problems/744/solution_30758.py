def hashtag(s):
    """ Função que insere caracter # no ínicio, no meio e no final dela
    str => str
    """
    str1 = "#" + str1[:len(s)//2] + "#" + str1[len(s)//2:] + "#"
    return str1