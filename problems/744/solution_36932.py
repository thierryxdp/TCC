def hashtag(s):
    metade = (len(s)//2)
    return '#' + s[0:metade] + '#' + s[metade:] + '#'