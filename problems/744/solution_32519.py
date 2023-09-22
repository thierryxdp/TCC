def hashtag(s):
    """A função retorna um '#' antes, no meio e ao final de uma determinada
    string. str--> str"""
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'