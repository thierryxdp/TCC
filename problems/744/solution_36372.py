def hashtag(s):
    x = len(s)//2
    nova_s = '#' + s[:x] + '#' + s[x+1:]
    return nova_s