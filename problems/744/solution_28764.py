def hashtag(s):
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    return '#' + a + '#' + b + '#'