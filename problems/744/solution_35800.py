def hashtag(s):
    charList = []
    
    for i in s:
        charList.append(i)
    
    charList.insert(int(len(charList)/2), "#")
    charList.insert(0, "#")
    charList.append("#")
    
    s = ""
    s = s.join(charList)
    
    return s