def hashtag(s):
    x = len(s)/2
    sub_s1 = s[0:x]
    sub_s2 = s[x:len(s)]
    return '#' + sub_s1 + '#' + sub_s2 + '#'