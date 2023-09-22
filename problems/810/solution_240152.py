def inverte(s):
    "//////////"
    s.replace(".", "")
    s.replace("?", "")
    s.replace("!", "")
    s.lower()
    lista  = str.split(s, " ")
    return str.join(" ", lista[::-1])