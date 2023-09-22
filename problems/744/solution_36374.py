def hashtag(s):
    x = len(s)//2
    nova_s = '#' + s[:x] + '#' + s[x:] + '#'
    return nova_s