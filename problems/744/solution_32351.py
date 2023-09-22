'''


:s -> str:
:return -> str:
'''
def hashtag(s):
    return s[:s] + str('#') + s[s:] + str('#')