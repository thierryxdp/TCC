def hashtag(s):
    """str->str"""
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s