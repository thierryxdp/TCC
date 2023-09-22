'''


:s -> str:
:return -> str:
'''
def hashtag(s):
    #pre = s[:len(s)//2]
    #pos = s[len(s)//2:]
    #s = "#" + pre + "#" + pos + "#"
    s = "#" + str1[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s