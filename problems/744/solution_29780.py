def hashtag(s):
    x=s[0:round(len (s))//2]
    y=s[round(len (s))//2:]
    return '''#'''+ x +'''#'''+ y +'''#'''