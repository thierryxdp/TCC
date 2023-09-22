def hashtag(s):
    inicio = s[:len(s)//2]
    final = s[len(s)//2:]
    s = "#" + inicio + "#" + final + "#"
    return s