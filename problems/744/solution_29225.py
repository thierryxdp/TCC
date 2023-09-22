def hashtag(s):
    """coloca "#" no inicio, meio e fim da palavra."""
    n = len(s)
    if (n%2 == 0):
        return("#"+s[0:(n//2)]+"#"+s[(n//2):]+"#")
    else:
        v = n//2
        return("#"+s[0:(v+1)]+"#"+s[(v+1):]+"#")