def hashtag(s):
    return '#' + s[0:len(str(s))//2] + '#' + s[len(str(s))//2:] + '#'