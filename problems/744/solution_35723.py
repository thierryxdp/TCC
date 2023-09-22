"""pre = str1[:len(str1)//2]
pos = str1[len(str1)//2:]
str1 = "#" + pre + "#" + pos + "#" """
# str-> str
def hashtag(s):
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1