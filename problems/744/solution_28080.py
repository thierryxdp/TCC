import math 
def hashtag(s):
    """"""
    n = math.floor(len(s)/2)
    z = n+1 
    return "#"+s[0:n]+"#"+s[z:]+"#"