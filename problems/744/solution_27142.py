def hashtag(s):
    # str-> str
    return str('#')+s[0:(len(s)//2)]+str('#')+s[(len(s)//2):]+str('#')