def hashtag(s):
    """Função que recebe uma string e insere um # no início, no meio e no final dela;
    str-> str"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s