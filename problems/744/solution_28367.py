def hashtag(s):
    t = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return t