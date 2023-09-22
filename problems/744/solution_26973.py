def hashtag(s):
    # str-> str
    a = len(s)//2 
    b = len(s)//2 + 1
    return '#'+ s[:a] + '#' + s[b:]