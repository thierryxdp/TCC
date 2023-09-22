def hashtag(s):
    """Dada uma string, retorna a string com o caractere # no inicio, meio e fim da #
    str -> str"""
    a = '#' + s[0:(len(s)//2)] + '#' + s[len(s)//2:] + '#'
    return a