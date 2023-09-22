def hashtag(s):
    """ Função que insere caracter # no ínicio, no meio e no final dela
    str => str
    """
    str1 = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return str1