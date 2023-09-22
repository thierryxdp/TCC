def hashtag(s):
    '''funcao que concatena # interladamente com a palavra que for inserida.'''
    '''str=>str'''
    meio=len(s)//2
    return '#' + str(s[0:meio]) + '#' + str(s[meio:]) + '#'