def hashtag (str1):
    pre = str1[:len(str1)//2]
    pos = str1[len(str1)//2:]
    str1 = "#" + pre + "#" + pos + "#"
    str1 = str1[:len(str1)//2] + "#" + str1[len(str1)//2:]
    return str1