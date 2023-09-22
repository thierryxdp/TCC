def hashtag(s):
    """i"""
    a= s[1,(len(s))/2] 
    b=s[(len(s))/2,(len(s))] 
    return '#'+ str(a)+ '#'+ str(b)+'#'