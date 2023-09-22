def hashtag(s):
    entre = len(s)//2
    result = "#" + s[:entre] + "#" + s[entre:] + "#"
    return result