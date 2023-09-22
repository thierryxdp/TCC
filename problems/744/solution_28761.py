def hashtag(s):
    """str -> str"""
    y = len(s)
    x = int(y / 2)
    z = '#' + str(s)[:x] + '#' + str(s)[x:] + '#'
    return z