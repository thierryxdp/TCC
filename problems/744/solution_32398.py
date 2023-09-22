'''


:s -> str:
:return -> str:
'''
def hashtag(s):
    return s[:0] + str('#') + str(s) + s[s:]