import math
def hashtag(s):
    """str -> str"""
    s = str(s)
    var1 = s[0:math.floor(len(s)/2)]
    var2 = s[math.floor(len(s)/2):len(s)]
    return '#' + var1 + '#' + var2 + '#'