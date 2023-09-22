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
    y = [str.split(str.lower(s))]
    return str (list.reverse (y))