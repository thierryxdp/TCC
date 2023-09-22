import math
def hashtag(s):
    mid = math.floor(len(s)/2)
    print ('#' + s[:mid] + '#' +s[mid:] +'#')