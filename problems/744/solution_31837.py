def hashtag(s):
    x = len(s)
    y = x/2
    sub_s1 = s[0:y]
    sub_s2 = s[y:x]
    return '#' + sub_s1 + '#' + sub_s2 + '#'