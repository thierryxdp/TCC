import math
def hashtag(s):
    mid = math.floor(len(s)/2)
    return '#' + s[:mid] + '#' + s[mid:] + '#'