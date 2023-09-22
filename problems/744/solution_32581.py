def hashtag(s):
    ''' funcao que retorna '#' no inicio, meio e fim atraves
        da colocao de cada letra do string s
        str -> str'''
    s= '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s