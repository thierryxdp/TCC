def hashtag(s):
    """..."""
    a = '#' + s[0:(len(s)//2)] + '#' + s[len(s)//2:] + '#'
    return a