def hashtag(s):
    '''Recebe um string e inseri uma # no inicio, meio e fim; str -> str'''
    x = floor(len(s)/2)
    return '#' + s[:x] + '#' + s[(x + 1):]