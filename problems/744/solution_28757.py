def hashtag(s):
    y = len(s)
    x = y / 2
    z = str('#') + str(s)[:x] + str('#') + str(s)[x:]
    return z