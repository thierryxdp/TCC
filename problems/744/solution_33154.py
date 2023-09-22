# str-> str
def hashtag(s):
    '''função que insere uma # no início, meio e fim de uma dada string s'''
    k = (len(s) // 2) 
    return '#' + s[0:k] + '#' + s[k:] + '#'