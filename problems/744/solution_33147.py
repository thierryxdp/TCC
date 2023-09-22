def hashtag(s):
    """Função que coloca # no inicio, meio e final de uma dada str.
       str->str"""
    meio=len(s)//2
    return '#' + str(s[0:meio]) + '#' + str(s[meio:]) + '#'