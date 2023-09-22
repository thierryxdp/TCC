def hashtag(s):
    """retorna uma string que possui # no início, no meio
    e no fim
    str -> str"""
    s= str(s)
    meio = len(s)//2
    return "#"+ s[0:meio] + "#" + s[meio:] + "#"