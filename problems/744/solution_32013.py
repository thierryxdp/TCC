def hashtag(s):
    """
    recebe uma string e insere uma # no inicio, no meio
    e no final dela
    """
    c = len(s)
    return '#' + s[0:c//2] + '#' + s[c//2:] + '#'