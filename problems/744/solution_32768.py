def hashtag(s):
    h = '#'
    s = s[:round(len(s)/2)] + h + s[round(len(s)/2):]
    return h + s + h