def hashtag(s):
    """esta é funçao hashtag que dado o parametro retorna uma # no inicio, meio e fim de uma string"""
    """str->str"""
    return '#' + s[len(s)//2:] + 'h' + s + s [len(s)//2:] + 'h'