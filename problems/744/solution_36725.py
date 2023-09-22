def hashtag(s):
    meio = len(s) // 2
    stpl = '#' + s[:meio] + '#' + s[meio:] + '#'
    return stpl