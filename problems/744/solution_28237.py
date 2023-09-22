def hashtag(s):
    """
    Essa funcao retorna a string com uma '#' no inicio meio e fim
    Parametros: s(string)
    saida: string
    """
    meio = (len(s)//2)
    r = "#" + s[0:meio] + "#" + s[meio:] + "#"
    return r