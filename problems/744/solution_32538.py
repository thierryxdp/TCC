def hashtag(s):
    '''a função inseri # no inicio, meio e fim da string. Str -> str'''
    return "#" + s[0:len(s)//2] + "#" + s[(len(s)//2)+1:len(s)] + "#"