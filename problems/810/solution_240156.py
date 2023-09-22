def inverte(s):
    "//////////"
    s = s.replace(".", "")
    s = s.replace("?", "")
    s = s.replace("!", "")
    s = s.replace(",", "")
    s = s.replace("-", "")
    s = s.lower()
    lista  = str.split(s, " ")
    return str.join(" ", lista[::-1])