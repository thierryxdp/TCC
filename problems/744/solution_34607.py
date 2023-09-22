from math import *
def hashtag(s):
    if len(s)% 2 != 0 :
        return "#"+ s[0:(floor((len(s))/2))] + "#" + s[ceil((len(s))/2)): ] + "#"
    else :
        if len(s)% 2 == 0 :
            return "#" + s[0: (len(s))/2] + "#" + s[len(s) /2 : ] + "#"