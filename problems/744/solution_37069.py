def hashtag(s):
    if len(s) % 2 == 0:
        return '#' + s[:(len(s)/2)] + '#' + s[(len(s)/2):] + '#'
    elif len(s) % 2 != 0:
        return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):] +'#'