def hashtag(s):
    '''Retorna uma string(s) com hashtag no início, no meio 
    e no fim
    string -> string '''
    x = '#'
    n = int(len(s)/2)
    return x+s[:n]+x+s[n:]+x