def hashtag(s):
    media = len(s) // 2
    return "#" + s[0:media] + s[:] + "#"