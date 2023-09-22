def hashtag(s):
    'posiciona uma # nas posiçoes inicio da str metade e final; str-> str'
    m = len(s)//2
    return '#' + s[0:m] + '#' + s[m:] + '#'