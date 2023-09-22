def hashtag(s):
    
    a= s[0:len(s)//2]
    b= s[len(s)//2:len(s)]
    
    return '#' + a + '#' + b + '#'