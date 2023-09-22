def hashtag(s):
    """retorna uma string com '#' no inicio, meio e fim dado a string original.
    str->str"""
    return '#' + str(s)[0:len(s)//2] + '#' + str(s)[len(s)//2:] + '#'