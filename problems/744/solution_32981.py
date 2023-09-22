def hashtag(s):
    '''
    '''
    caract_s = len(s)
    meio = caract_s//2
    meio1 = s[0:meio]
    meio2 = s[meio:caract_s]
    return '#' + meio1 + '#' + meio2 + '#'