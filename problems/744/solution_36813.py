def hashtag(s):
    meio = len(s) // 2
    stp1 = '#' + s[:meio] + '#' + s[meio:] + '#'
    return stp1