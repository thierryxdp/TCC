def hashtag(s):
    """ uma string inserida de # no início meio e fim
    str-> str"""
    metade = Ien (s) // 2 
    return '#' + s [:metade] + '#' + s [metade:] + '#'