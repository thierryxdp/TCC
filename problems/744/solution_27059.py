def hashtag(s):
    
    x = int(len(s)/2)
    
    if len(s)%2 == 0:
        
        return "#"+s[0:x]+"#"+s[x:]
    
    else:
        
        return "#"+s[0:x]+"#"+s[x:]