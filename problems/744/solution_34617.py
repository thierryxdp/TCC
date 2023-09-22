from math import *
def hashtag(s):
    if len(s)% 2 != 0 :
        return "#"+ str(s[0:(ceil((len(s))/2)))]) + "#" + str(s[(floot(len(s)))/2): ]) + "#"
    else :
        if len(s)% 2 == 0 :
            return "#" + str(s[0: (len(s))/2]) + "#" + str (s[len(s) /2 : ]) + "#"