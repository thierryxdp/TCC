"""pre = str1[:len(str1)//2]
pos = str1[len(str1)//2:]
str1 = "#" + pre + "#" + pos + "#" """
# str-> str
def hashtag(s):
    str = "#" + str[:len(str)//2] + "#" + str[len(str)//2:] + "#"
    return str1