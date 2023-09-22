def hashtag(s):
    # str-> str
    if len(s)%2 == 0:
        meio = len(s) / 2
    else:
        meio = math.ceil((len(s)+2)/2 - 1)
    string = list(s)
    string.insert(0, '#')
    string.insert(meio, '#')
    string.append('#')
    string = "".join(string)
    return string