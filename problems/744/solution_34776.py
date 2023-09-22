def hashtag(s):
    x = int(len(s)/2)
    return '#' + s [:x] + '#' + s[x:] + '#'