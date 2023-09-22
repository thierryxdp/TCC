def inverte(s):
    if "-" in s:
     s = str.replace (s,"-", " ")
    if "," in s:
     s = str.replace (s, ",", " ")
    if ":" in s:
     s = str.replace (s, ":", " ")
    if ";" in s:
     s = str.replace (s, ";", " ")
    if "." in s:
     s = str.replace (s, ".", " ")
    if "?" in s:
     s = str.replace (s, "?", " ")
    if "!" in s:
     s = str.replace (s, "!", " ")
    s = (str.split(str.lower(s)))
    list.reverse(s)
    z = ' '
    return z.join(s)