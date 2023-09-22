def hashtag(s):
    antes = s[:len(s)//2]
    depois= s[len(s)//2:]
    s = "#" + antes + "#" + depois + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s