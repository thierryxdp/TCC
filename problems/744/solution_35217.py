def hashtag(s):
    l = len(s)
    return "#" + s[0:l/2] + "#" + s[l/s:] + "#"