def hashtag(s):
"""str-> str"""
    y = len(s) / 2
    z = str('#') + str(s)[:y] + str('#') + str(s)[y:]
    return z