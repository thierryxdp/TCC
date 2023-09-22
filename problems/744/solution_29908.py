def hashtag(s):
    """ String que compacta "#" no inicio, no meio o no fim da mesma
    str -> str"""
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'