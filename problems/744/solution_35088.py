def hashtag(s):
    nova_string = 'a' + s[:len(s)//2:]+ 'c'
    + s[len(s)//2:] + '#'
    return nova_string