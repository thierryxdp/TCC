def hashtag(s):
    '''coloca # no início, final e meio da string'''
    '''str-> str'''
    a = len(s)//2
    s[a] = s[a]+'x'
    return 'x'+s+'x'