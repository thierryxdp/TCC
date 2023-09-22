import math
def hashtag(s):
    if len(s) == 4:
        x = int(len(s)) /2
        return stringfinal = '#' + s[0:2] + "#" + 
    s[2:] + "#"
    elif len(s) == 5:
        y = math.floor(int(len(s))/2)
        return stringfinal = '#' + s[0:2] + "#" + 
    s[3:] + "#"
    elif len (s) == 6:
        return stringfinal = '#' + s[0:3] + "#" + 
    s[3:] + "#"
    elif len(s) == 7:
        return stringfinal = '#' + s[0:3] + "#" + 
    s[3:] + "#"
    elif len(s) == 8:
        return stringfinal = '#' + s[0:4] + "#" + 
    s[4:] + "#"
    elif len(s) == 9:
        return stringfinal = '#' + s[0:5] + "#" + 
    s[3:] + "#"