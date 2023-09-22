def hashtag(s):
    x=len(s)//2
    return str('#')+s[:x]+str('#')+s[x:]+str('#')