def hashtag(s):
    s=str(s)
    meio=len(s)//2
    com=len(s)/2
    return "#"+s[com:meio:]+"#"