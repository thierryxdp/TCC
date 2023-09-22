def hashtag(s):
    y = len(s)
    x = y / 2
    z = '#' + str(s)[:x] + '#' + str(s)[x:]
    return z