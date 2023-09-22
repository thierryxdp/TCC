import math 
def hashtag(s):
    """"""
    n = math.floor(len(s)/2)
    return "#"+s[0:n]+"#"+s[n:]+"#"