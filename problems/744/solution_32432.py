def hashtag(s):
    ''' Retorna uma string com # no início, no meio 
    e no final dela '''
    # s[0:len(s)//2] + "#" + [len(s)//2:0]
    return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:0] + "#"