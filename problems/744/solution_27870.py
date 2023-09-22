def hashtag(s):
    pos_meio= len(s)//2
    return "#"+s[0:pos_meio]+"#"+s[pos_meio:]+"#"