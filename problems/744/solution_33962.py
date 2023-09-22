from math import *
def hashtag(s):
    metade_str1 = len (s)/2
    metade_str2 = floor (metade_str1)
    return '#' + s[0:metade_str2] + '#' + s[metade_str2:] + '#'