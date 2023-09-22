def hashtag(s):
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:len(s)]
    return ('#' + s1 + '#' + s2 + '#')