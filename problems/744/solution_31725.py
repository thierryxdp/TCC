def hashtag(s):
    '''Hashtag é uma função que coloca # no início, no meio e no fim de uma string,
(string->string)'''
    s="#"+s[0:(len(s)//2)]+"#"+s[(len(s)//2):len(s)]+"#"
    return s