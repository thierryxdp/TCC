import math
def hashtag(s):
    if lens(s)% 2==0:
        x = int(lens(s)) /2
        return stringfinal = '#' + s[0:int(x)] + "#" + 
    s[int(x):] + "#"
    else:
        y = math.floor(int(lens(s))/2)
        return stringfinal = '#' + s[0:int(y)] + "#" + 
    s[int(y):] + "#"