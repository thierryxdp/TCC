def freq_palavras(string):
    """doc"""
    palavras = string.split()
    dic = {}
    for palavra in list(set(palavras)):
        dic[palavra] = palavras.count(palavra)
    return dic