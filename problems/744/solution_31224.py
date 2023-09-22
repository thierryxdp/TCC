def hashtag(s):
    """Uma função que recebe uma string e insere o caractere '#' no inicio, no meio e no final dela;
    str-->str"""
    import math
    def hashtag(s):
    if(len(s)==0):
        return '###'
    else:
        x = len(s)
        s = s[0:(math.floor(x/2))] + '#' + s[(math.floor(x/2)):-1] + s[-1]
        s = '#' + s
        s = s + '#'
        return s