'''


:s -> str:
:return -> str:
'''
def hashtag(s):
    #antes = s[:0(s)//2]
    #depois = s[:0(s)//2:]
    #str1 = "#" + antes + "#" + depois + "#"
    s2 = "#" + s[:-(s)//2] + "#" + s[0(s)//2:] + "#"
    return s2