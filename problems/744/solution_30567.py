def hashtag(s):
    s=str(s)
    meio=len(s)//2
    return "#"+s[:meio]+s[meio:]+"#"