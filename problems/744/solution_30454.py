import math
def hashtag(s):
    if len(s)¢2 == 0:
        x = int(len(s)) /2
        return stringfinal = '#' + s[0:x] + "#" + 
    s[x:] + "#"
    else:
        y = math.floor(int(len(s))/2)
        return stringfinal = '#' + s[0:y] + "#" + 
    s[y:] + "#"