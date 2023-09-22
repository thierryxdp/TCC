def hashtag(s):
        h= "h"
        s = h + s[:len(s)//2] + h + s[len(s)//2:] + h
    return s