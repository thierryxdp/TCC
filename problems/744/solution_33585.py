def hashtag (s):

    m = round (len(s)/2)
    s = '#' + s[:m] + '#'+ s[m:]+ '#'
    return s