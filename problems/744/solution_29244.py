def hashtag(s):
    x=len(s)
    return "#"+s[0:(x//2)]+"#"+s[(x//2):]+"#"