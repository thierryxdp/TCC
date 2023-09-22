def hashtag(s):
    half = len(s)// 2 
    newcaracter "#" + s [:half] + "#" + s[half:] + "#"
    return newcaracter