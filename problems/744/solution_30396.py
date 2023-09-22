def hashtag(s):
    def ex6_hashtag(str1):
        h= "h"
        s = h+ s[:len(s)//2] + h + s[len(s)//2:] + h
    return s