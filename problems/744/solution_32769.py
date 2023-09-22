def hashtag(s):
    h = '#'
    t = int(len(s)/2)
    s = s[:t] + h + s[t:]
    return h + s + h