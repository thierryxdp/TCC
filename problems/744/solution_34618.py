from math import *
def hashtag(s):
    return "#" + s[0: (floot((len(s))/2)) ] + "#" + s[(floot(len(s))/2):] + "#"