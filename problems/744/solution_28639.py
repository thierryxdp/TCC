def hashtag(s):
    """função que recebe uma string e retorna a string com # no inicio meio e fim.
    str->str"""
    i = len(s)//2
    
    return ("#"+s[0:i]+"#"+s[i+1:]+"#")