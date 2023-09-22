def hashtag(s):
    #pre = s[:len(str1)//2]
    #pos = s[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(str1)//2] + "#" + s[len(s)//2:] + "#"
    return s1