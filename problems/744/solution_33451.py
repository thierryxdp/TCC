def hashtag(s):
    '''Escreva uma funcão que receba ''#'' no inicio, meio e fim'''
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = '#' + pre + '#' + pos + '#'
    str1 = '#' + str1[:len(str1)//2] + '#' + str1[len(str1)//2:] + '#'
    return str1