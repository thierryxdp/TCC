def hashtag(s):
    '''insere uma hashtag no início, no meio e no final
    da string s'''
    h='#'
    m= len(s)//2
    met1= s[0:m]
    met2= s[m:len(s)]
    return h + met1 + h + met2 + h