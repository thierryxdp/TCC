def hashtag(s):
    i=0 
    r=''
    x=((len(s)-1)//2)
    y=''
    while i < (len(s)-1)/2:
        r = r + s[i]
        i = i + 1
    
    while x < len(s):
        y = y + s[x]
        x = x + 1
        
    return y