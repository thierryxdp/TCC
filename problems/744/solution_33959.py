def hashtag(s):
    metade_string = len(s)%2
    return '#' + s[0:metade_string] + '#' + s[metade_string:] + '#'