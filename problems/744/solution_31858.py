def hashtag(s):
    s1 = [0:len(s)//2]
    s2 = [len(s)//2:len(s)]
    return ('#' + s1 + '#' + s2 + '#')