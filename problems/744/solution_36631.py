def hashtag(s):
    '''retoma a palavra com hashtag no inicio, no meio e no fim.
    str --> str'''
    
    caracter_meio = len(s)//2
    pt1 = s[0:carcter_meio]
    pt2 = s[caracter_meio: len(s)]
    return 'hashtag' + pt1 + 'hashtag' + pt2 + 'hashtag'