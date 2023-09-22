import math

def hashtag(s):
    """recebe uma string e retorna essa mesma string, mas com # em seu inicio, meio e final"""
    
    x = len(s)
    x = math.floor(x)
    
    s1, s2 = s[:(x / 2)], s[(x / 2):]
    
    return '#' + s1 + '#' + s2 + '#'