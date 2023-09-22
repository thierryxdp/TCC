def hashtag(s):
    """retorna uma string que possui # no início, no meio
    e no fim
    str -> str"""
    s= str(s)
    return "#"+ s[0:2] + "#" s[2:] + "#"