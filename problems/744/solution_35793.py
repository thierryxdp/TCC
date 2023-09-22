def hashtag(s):
    i=int (len(s)/2)
    return '#' + s[0:i] + '#' + s[i:i+1] + s[i+1:] + '#'