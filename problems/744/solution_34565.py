def hashtag(s):
    """Função que recebe uma string e insere um # no início, no meio e no final dela;
    str-> str"""
    str = "#" + str[:len(str)//2] + "#" + str[len(str)//2:] + "#"
    return str