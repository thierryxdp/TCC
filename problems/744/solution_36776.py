def hashtag(s):
    meio = len(s)// 2 
    newcaracter '#' + s[:meio] + '#' + s[meio:] + '#'
    return newcaracter