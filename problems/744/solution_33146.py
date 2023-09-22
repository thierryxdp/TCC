def hashtag(s):
    """Função que coloca # no inicio, meio e final de uma dada str.
       str->str"""
    return '#' + str(s[0:len(s)/2) + '#' + str(s[len(s)/2 + 1:]) + '#'