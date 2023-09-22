from math import *
def hashtag(s):
        return '#' + s[:floor(len(s)/2)] + '#' + s[floor(len(s)/2):] + '#'