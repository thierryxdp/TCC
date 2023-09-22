def hashtag(insta):
    str1 = insta
    str2 = "#"
    return str2 + str1[0:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):len(str1)+1] + str2