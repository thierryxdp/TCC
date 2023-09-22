def hashtag(s):
    '''A função colocará 3 hashtags nos caracteres inseridos: No início,
    no meio e no final no texto inserido.
    string -> string'''
    Qs = len(s)
    m = Qs//2
    metade1 = s[0:m]
    metade2 = s[m:-1]
    
    return '#' + metade1 + '#' + metade2 + '#'