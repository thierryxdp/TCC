def hashtag(s):
    """retorna uma strin com # no inicio, meio e fim
    str->str"""
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'