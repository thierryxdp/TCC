def hashtag(s):
    '''Retorna a string inserida com # antes, no meio e no final dela.
    str -> str'''
    return "#" + str(s)[0:(len(s)//2)] + "#" + str(s)[len(s)//2:len(s)] + "#"