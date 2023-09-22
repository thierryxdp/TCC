import math
from math import *
def hashtag(s):
    x= len(s)/2
    return '#' + s[:int(x)]+'#'+s[int(x):]+'#'