def hashtag(s):
    """ uma string inserida de # no início meio e fim
    str-> str"""
    metade = len (s) // 2 
    return '#' + s [:metade] + '#' + s [metade:] + '#'