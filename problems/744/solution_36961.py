def hashtag(s):
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#' + s[len(s)//2]
    return s