def hashtag(s):
    meio = len(s) // 2
    sptl = "#" + s[:meio] + "#" s[meio:] + "#"
    return sptl