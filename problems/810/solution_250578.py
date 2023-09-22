def inverte (s):
    if "." in s:
        s = str.replace (s, ".", " ")
    if "," in s:
        s = str.replace (s, ",", " ")
    if ":" in s:
        s = str.replace (s, ":", " ")
    if ";" in s:
        s = str.replace (s, ";", " ")
    if "-" in s:
        s = str.replace (s, "-", " ")
    if "!" in s:
        s = str.replace (s, "!", " ")
    if "?" in s:
        s = str.replace (s, "?", " ")
    y = str.split(str.lower(s))
    list.reverse (y)
    z = " "
    return z.join(y)