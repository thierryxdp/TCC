def hashtag(s):
    return "#"+s[0:math.floor(len(s)/2)]+"#"+s[math.floor(len(s)/2):]+"#"